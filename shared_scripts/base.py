'''
Created on 23 Apr 2015

@author: balaji.chandrababu
'''

import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os, sys
import utils
import time
import string

class DriverInstance(object):
    global_driver = None # using singleton pattern to initiate the webdriver only once for running all the test cases
      
    def __init__(self):
        if DriverInstance.global_driver is None:
            DriverInstance.global_driver = webdriver.Firefox()
            DriverInstance.global_driver.implicitly_wait(30)
            DriverInstance.global_driver.get("http://www.hudl.com/")
        self.driver = DriverInstance.global_driver
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def login(self, username, password):
        login = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "html/body/header/section[1]/div/a")))
        login.click()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("logIn").click()
  
    def test_roster_menu(self):
        self.driver.find_element_by_link_text("Team").click()
        self.driver.find_element_by_link_text("Roster").click()
        element = self.driver.find_element_by_xpath(".//*[@id='pageContent']/div[1]/div[1]/h1")
        assert element.text == "Manage Roster", "Manage Roster Page has been loaded"
  
    def test_export_roster(self):
        self.driver.find_element_by_id("export_roster").click()
        export_script_path = os.path.join(utils.get_cwd(), "resources\\AutoIt_Script_Export.exe")
        os.system(export_script_path)
      
    def test_import_roster(self):
        self.driver.find_element_by_id("upload_new_roster").click()
        self.driver.find_element_by_id("RosterFileUpload").click()
        import_script_path = os.path.join(utils.get_cwd(), "resources\\AutoIt_Script_Import.exe")
        os.system(import_script_path)
        
    def test_validate_import_roster_data(self):
        athlete_count = 1
        upload_dialog = self.driver.find_element_by_id("upload_dialog")
        if upload_dialog.is_displayed():
            no_of_athletes = self.driver.find_element_by_id("entries_count")
            no_of_athletes = no_of_athletes.text
            print no_of_athletes
            try:
                while athlete_count <= int(no_of_athletes):
                    athlete_href_link = self.driver.find_element_by_class_name("next")
                    athlete_href_link.click()    
                    athlete_count = athlete_count + 1   
                upload_next = self.driver.find_element_by_id("uploadNext").click()
            except NoSuchElementException:
                return False
        else:
            print upload_dialog + "doesn't appear. Hence the import Roster test failed"
        import_success_message = self.driver.find_element_by_id("import_progress_message")
        assert import_success_message.text == "Done importing your roster! Reload the page to see your updated roster.", import_success_message.text
        page_reload = self.driver.find_element_by_link_text("Reload the page")
        page_reload.click()
        
    def test_verify_athlete_detail(self, first_name, last_name, gmail_id):
        # list of required field objects
        required_fields = ["first_name_validation","last_name_validation"]
        # dict of input fields key value pairs
        input_fields = [("first_name",first_name), ("last_name",last_name)]
        add_athlete_button = self.driver.find_element_by_css_selector("span.unitPng")
        add_athlete_button.click()
        # Validating whether the first and last names are required fields
        for field in required_fields:
            name = self.driver.find_element_by_id(field)
            assert name.text == "Required", name.text
        # checking whether adding an new/existing athlete details creates a new profile
        for i in range(2):
            DriverInstance.test_add_athlete(self, input_fields, add_athlete_button, first_name, last_name, gmail_id, i)
            if i == 1:
                notification = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.normal")))
                assert notification.text == "That athlete is already on that roster", notification.text 
            else:
                pass
    
    def test_add_athlete(self, input_fields, add_athlete_button, first_name, last_name, gmail_id, i):
        for input in input_fields:
            self.driver.find_element_by_id(input[0]).clear()
            self.driver.find_element_by_id(input[0]).send_keys(input[1])
        self.driver.find_element_by_id("jersey").clear()
        self.driver.find_element_by_id("jersey").send_keys("22")
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(gmail_id+"@gmail.com")
        header_grad_year = self.driver.find_element_by_id("class")
        utils.get_parent_element(header_grad_year)
        if i == 0:
            self.driver.find_element_by_css_selector("span.dropDownButton").click()
            self.driver.find_element_by_id("new_pos_RB").click()
            self.driver.find_element_by_id("new_pos_SB").click()
        else:
            # due to dropdownmenu object changes 
            self.driver.find_element_by_id("position").click()
            self.driver.find_element_by_id("new_pos_RB").click()
            self.driver.find_element_by_id("new_pos_SB").click()
        add_athlete_button.click()
        
    def test_edit_athlete_details(self, athlete_id):
        athlete_id = string.split(athlete_id, "_")
        athlete_data = [("edit_cell_number", "07514576987"), ("edit_home_number", "02056542589"), ("edit_street", "brent lane"),
                        ("edit_city", "London"), ("edit_state", "London"), ("edit_postal_code", "NW23 4TY"), ("edit_parents_name", "Hudl Test User"), 
                        ("edit_parents_number", "07514576987"), ("edit_height", "5"), ("edit_inches", "13"), ("edit_weight", "85"), ("edit_additional_notes", "Locker No: 34")]
        image_autoit_script = ["AutoIt_Script_Upload_Image_png.exe", "AutoIt_Script_Upload_Image_jpeg.exe", 
                               "AutoIt_Script_Upload_Image_bmp.exe", "AutoIt_Script_Upload_Image_gif.exe"]
        for data in athlete_data:
            self.driver.find_element_by_id(data[0]).clear()
            self.driver.find_element_by_id(data[0]).send_keys(data[1])
        Select(self.driver.find_element_by_id("edit_cell_carrier")).select_by_visible_text("Virgin Mobile")
        self.driver.find_element_by_xpath(".//*[@id='edit_remove_season']/li/a").click()
        Select(self.driver.find_element_by_id("edit_add_season")).select_by_visible_text("2013-2014")
        self.driver.find_element_by_id("edit_save_changes").click()
        cell_number = self.driver.find_element_by_id("edit_cell_number_validation")
        assert cell_number.text == "Use 10-digit number (eg. 4025550000)", cell_number.text
        self.driver.find_element_by_id("edit_cell_number").clear()
        self.driver.find_element_by_id("edit_cell_number").send_keys("0751457698")
        self.driver.find_element_by_id("edit_save_changes").click()
        # Testing whether png, jpg, bmp, gif images can be uploaded
        for script in image_autoit_script:
            time.sleep(4)
            utils.mouse_move_over(athlete_id[1], ".//*[@id='roster-image-"+athlete_id[1]+"']", self.driver)
            edit_image = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#edit-image-"+athlete_id[1]+" > span")))
            edit_image.click()
            self.driver.find_element_by_xpath(".//*[@id='file-uploader']/div/div[2]/input").click()
            upload_image_script_path = os.path.join(utils.get_cwd(), "resources\\"+script)
            os.system(upload_image_script_path)
            upload_image_dialog = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#AjaxUploadImageDialog-dialog > div.footer > #changeImageSave")))
            upload_image_dialog.click()
#             notification = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.normal")))
#             assert notification.text == "Huzzah! Check out your new picture.", notification.text
            
    def test_search_athlete_detail(self, first_name, last_name, gmail_id):
        search_data = [first_name, last_name, gmail_id+"@gmail.com", "rb,sb", "2013", first_name+"."+last_name]
        for data in search_data:
            self.driver.find_element_by_id("search").clear()
            self.driver.find_element_by_id("search").send_keys(data)
            if str(data) != gmail_id+"@gmail.com" or "rb,sb" or "2013":
                print "Search results found: "+data
            else:
                no_players = self.driver.find_element_by_id("no_players")
                assert no_players.text == "No athletes match your search ", no_players.text 
        gmail_id = gmail_id+"@gmail.com" 
        # Using javascript fucntion to get the athlete id of the search result 
        get_athlete_id_using_js = "var id_value; function myFunction(elem) {  for (i = 0; i < elem.length; i++) {   if (elem[i].innerHTML === '"+gmail_id+"') { id_value = elem[i].parentElement.parentNode.id; } } return id_value; } var elem = document.querySelectorAll('p.email'); return myFunction(elem);"
        athlete_id = self.driver.execute_script(get_athlete_id_using_js)
        # function to hover the mouse over search result so that the edit link is clickable
        utils.mouse_move_over(athlete_id, ".//*[@id='"+str(athlete_id)+"']", self.driver)
        edit_player_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#"+str(athlete_id)+" > div.edit > a.edit_player_link")))
        edit_player_link.click()
        DriverInstance.test_edit_athlete_details(self, str(athlete_id))
        utils.mouse_move_over(athlete_id, ".//*[@id='"+str(athlete_id)+"']", self.driver)
        toggle_disabled_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#"+str(athlete_id)+" > div.edit > a.toggle_disabled_link")))
        toggle_disabled_link.click()
        self.driver.find_element_by_link_text("Enable").click()
        utils.mouse_move_over(athlete_id, ".//*[@id='"+str(athlete_id)+"']", self.driver)
        self.driver.find_element_by_xpath(".//*[@id='"+str(athlete_id)+"']/div[6]/a[3]/img").click()
        self.driver.find_element_by_id("delete_from_team").click()

if __name__ == "__main__":
    unittest.main()