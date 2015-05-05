'''
Created on 23 Apr 2015

@author: balaji.chandrababu
'''

from ConfigParser import SafeConfigParser
import codecs
from os.path import dirname
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


def read_credentials_from_config(): # function to retrieve and parse data from the config file
    parser = SafeConfigParser()
    source_dir = get_cwd()
    config_file_path = os.path.join(source_dir, "ConfigFile\\Hudl.credentials")
    print config_file_path
    with codecs.open(config_file_path, 'rb', encoding='utf-8') as f:
        parser.readfp(f)
    user_name = parser.get("Credentials","username")
    password = parser.get("Credentials", "password")
    first_name = parser.get("Credentials", "first_name")
    gmail_last_name = parser.get("Credentials", "last_name")
    last_name = gmail_last_name + "_" +str(int(time.time()))
    gmail_id = first_name+"."+gmail_last_name+"+Invite"+str(int(time.time())) 
    return user_name, password, first_name, last_name, gmail_id

def get_cwd(): # used for getting the current working directory
    parent_dir = dirname(dirname(__file__))
    return parent_dir
    
def get_parent_element(header): # iterate through the child nodes and select them
    all_children_by_xpath = header.find_elements_by_xpath(".//*")
    print 'len(all_children_by_xpath): ' + str(len(all_children_by_xpath))
    for element in all_children_by_xpath:
        element.click()
            
def mouse_move_over(athlete_id, xpath_id, driver): # move the mouse to enable hidden links
    mouse_move = driver.find_element_by_xpath(xpath_id)
    hover = ActionChains(driver).move_to_element(mouse_move)
    hover.perform()
    