from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_log
import logging


class LoginPage(SeleniumDriver):

    log = custom_log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    _login_link = '//a[contains(text(),"Login")]'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'
    _search_course_field = 'search-courses'
    _login_error = '//div[contains(text(),"Invalid email or password")]'

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.element_click(LoginPage._login_link, locatortype='xpath')

    def enterUserName(self, username):
        # self.getEmailField().send_keys(username)
        self.enter_text(username,LoginPage._email_field)

    def enterPassword(self, password):
        # self.getPassField().send_keys(password)
        self.enter_text(password, LoginPage._pass_field)

    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.element_click(LoginPage._login_button,locatortype='name')

    def verifyLoginSuccess(self):
        result = self.is_element_present(LoginPage._search_course_field)
        return result

    def verifyLoginFailed(self):
        result = self.is_element_present(LoginPage._login_error,locatortype='xpath')
        return result

    def clearLoginFields(self):
        emailField = self.get_element(LoginPage._email_field)
        emailField.clear()
        passField = self.get_element(LoginPage._pass_field)
        passField.clear()


    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()
