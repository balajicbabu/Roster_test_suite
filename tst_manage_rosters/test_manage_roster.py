    # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import utils
import base
"""
This is the main class which acts as a test suite and executes all the test cases one by one 
"""

class ManageRostersWebPage(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = base.DriverInstance()
#         
    def test_manage_roster(self):
        username, password, first_name, last_name, gmail_id = utils.read_credentials_from_config()
        self.driver.login(username, password)
        self.driver.test_roster_menu()
        self.driver.test_export_roster()
        self.driver.test_import_roster()
        self.driver.test_validate_import_roster_data()
        self.driver.test_verify_athlete_detail(first_name, last_name, gmail_id)
        self.driver.test_search_athlete_detail(first_name, last_name, gmail_id)
        
if __name__ == "__main__":
    unittest.main()