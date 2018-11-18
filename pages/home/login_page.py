from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    _login_link = '//a[contains(text(),"Login")]'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'



    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, LoginPage._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, LoginPage._email_field)
    #
    # def getPassField(self):
    #     return self.driver.find_element(By.ID, LoginPage._pass_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, LoginPage._login_button)

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.element_click(LoginPage._login_link, locatortype='xpath')

    def enterUserName(self, username):
        # self.getEmailField().send_keys(username)
        self.enter_text(username,LoginPage._email_field)

    def enterPassword(self, password):
        # self.getPassField().send_keys(password)
        self.enter_text(password, LoginPage._pass_field)

    def loginButton(self):
        # self.getLoginButton().click()
        self.element_click(LoginPage._login_button,locatortype='name')

    def login(self, username, password):

        self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.loginButton()

