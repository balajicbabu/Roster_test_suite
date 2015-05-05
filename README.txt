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
4) AutoIt tool installed. (Please select this link or copy-paste into your web browser to download https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe)

Steps to open and Execute the Project in Eclipse:

1) Click on File --> Import
2) Select Existing projects into your workspace.
3) Right-click on the project, and select Properties. Select PyDev-PYTHONPATH. 
4) Click on Add Source Folder. Add /${PROJECT_DIR_NAME}/shared_scripts and /${PROJECT_DIR_NAME}/ConfigFile into PYTHONPATH.
5) If you have all the above pre-requisites, you should be able to run the tests using "Python Run" or "Python Unit-test" without any issues.

Scenarios Automated:

1) Login to Hudl Account using right credentials.
2) Import Roster
3) Export Roster
4) Validate import roster data
5) Upload profile picture for search result data (athlete).
6) Disable/Enable the athlete from the team
7) Delete the athlete from the team