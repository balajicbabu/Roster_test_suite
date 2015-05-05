# Roster_test_suite

Roster Test Suite

This project consists of several automated tests covering the Manage Roster page.

It runs on the hudl website (www.hudl.com)

Important Source Files:

test_manage_roster.py - Main class which acts as a test suite to execute all the test cases

Shared Scripts: Contains support modules
	- base.py - Contains the webdriver instance and all the test cases (functions)
	- utils.py - Contains all the supported functions which drives the tests

resources: A directory which contains:
	- File(xlsx) for exporting into roster database.
	- Images (png, jpg, bmp, gif) for updating the athlete profile picture.
	- Autoit(au3) files contains scripts which will automate the windows browser events (For instance: Import/Export, uploading images)
	- Autoit(exe) files - au3 files which was created using Autoit tool and that has been transformed into exe files which is later being executed in the test cases using python built-in modules.
	
Third-Party Tool:
- AutoIt is just another automation tool like Selenium but unlike Selenium it is used for Desktop Automation rather Web Automation.  
It is a powerful tool and it just not automate desktop windows, button & form, it automates mouse movements & keystrokes too. 

Pre-requisites:

1) Use Python 2.7. (Tests can be executed in Python 3 as well. But for the info, tests were written and executed using Python 2.7.6)
2) Eclipse IDE (PyDev Plugin installed) 
3) Selenium Webdriver 2.0
