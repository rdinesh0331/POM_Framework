from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    #locators

    _login_link = '//a[contains(text(),"Login")]'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, LoginPage._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, LoginPage._email_field)

    def getPassField(self):
        return self.driver.find_element(By.ID, LoginPage._pass_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, LoginPage._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterUserName(self, username):
        self.getEmailField().send_keys(username)

    def enterPassword(self, password):
        self.getPassField().send_keys(password)

    def loginButton(self):
        self.getLoginButton().click()

    def login(self, username, password):

        self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.loginButton()

