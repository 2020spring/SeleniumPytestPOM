# Sample Selenium pytest project using POM design pattern

## Project structure: 

    README.md
        description of the project
        Instructions
        requirements 
        
    data (input)
    screenshots
    logs
    src (source code in this package)
        - features (enhancement with bdd)
        - pages (enhancement with POM)
        - steps (enhancement with POM)
    
        - tests (package)
            <login_to_automation_practice>
        - conftest.py
        - utilities.py (commonly used functions not from selenium)
            loading yml
            save root dir
            take screenshots
            create logging 	
            
        - Import all files and import one file for all tests
            all_imports.py
                import yaml
                from os.path import dirname, abspath
    
                from selenium.webdriver import ActionChains
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                
            login.py
                from src.all_imports import *
                
      requirements.txt () - list of all required libraries for the project

## References: 
1. link to help you with identifying the locators [check here.](https://www.red-gate.com/simple-talk/dotnet/.net-framework/xpath,-css,-dom-and-selenium-the-rosetta-stone/)