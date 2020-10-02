from src.all_imports import *

data = utils.load_yaml(f"{utils.ROOT_DIR}/data/config.yml")
data_neg = utils.load_yaml(f"{utils.ROOT_DIR}/data/login_scenarios/login_negative.yml")


@pytest.mark.login
@pytest.mark.loginPositive
def test_login_case1(driver):
    # print("This is it, I am doing my first Framework!!")
    utils.LOG.info("test_login_case1 started ...")
    # utils.LOG.debug("Debug message....")
    # utils.LOG.error("I am an exceptional case.")
    # utils.LOG.warning("something does not seem to be right, but not an error.")
    # utils.LOG.critical("WOUUW WOOUW STOP NOW, CAN NOT RUN ANYTHING AT THIS POINT!!!!")

    web_url = data['scenario1']['web_url']
    username = data['scenario1']['username']
    pswd = data['scenario1']['password']

    login_page = LoginPage(driver)

    driver.get(web_url)
    print(f"opened the browser and website : {web_url}")
    time.sleep(1)  # thread.sleep() in java

    login_page.click_sign_in_link()
    login_page.enter_email(username)
    login_page.enter_password(pswd)
    login_page.click_sign_in_button()
    utils.LOG.info("We are able to sign in now.")
    time.sleep(5)
    # assert login_page.get_app_message() == 'enter correct pssword'
    login_page.take_screenshot('HomePage-')

    login_page.sign_out()
    utils.LOG.info("test_login_case1 completed ")


@pytest.mark.login
@pytest.mark.loginNegative
def test_login_case2(driver):
    pass
    web_url = data_neg['scenario1']['web_url']
    username = data_neg['scenario1']['username']
    pswd = data_neg['scenario1']['password']