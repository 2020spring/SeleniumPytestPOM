from src.all_imports import *

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)  # read more about this


# def launch_website(url):
#     driver.get(url)
#     print(f"opened the browser and website : {url}")
#     time.sleep(1)  # thread.sleep() in java
#
#
# def login_to_automation_practice(url, email, password):
#     """
#     *********** Scenario: Login to "http://automationpractice.com/index.php"
#     Prerequisite: create an account:
#     username: hello@email.com, have strong password: "$Password001"
#     identify all locators by inspecting on browser (xpath, optional: id, css selector):
#     sign_in_link = "//a[@class='login'" # this is incorrect XPATH, to see Try Except
#     """
#
#     sign_in_link = "//a[@class='login']"
#     email_input = "//input[@id='email']"
#     password_input = "//input[@id='passwd']"
#     sign_in_button = "//button[@id='SubmitLogin']"
#     sign_out_link = "//a[@class='logout']"
#
#     # Steps:
#     launch_website(url)
#     click_element_by_xpath(sign_in_link)
#     time.sleep(2)
#     enter_text_by_xpath(email_input, email)
#     enter_text_by_xpath(password_input, password)
#     click_element_by_xpath(sign_in_button)
#     time.sleep(10)
#     utils.LOG.info("successfully signed in ")
#     utils.LOG.info("signing out now...")
#     click_element_by_xpath(sign_out_link)
