from selenium import webdriver
from pages.home.login_page import LoginPage as lp
import unittest
from utilities.custom_logger import custom_log
import logging
import pytest
import time


class LoginTests(unittest.TestCase):

    log = custom_log(logging.INFO)

    base_url = 'https://learn.letskodeit.com/p/practice'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    test_obj = lp(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        LoginTests.driver.get(LoginTests.base_url)
        LoginTests.test_obj.login('test@email.com', 'abcabc')
        result = LoginTests.test_obj.verifyLoginSuccess()
        assert result == True
        LoginTests.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        LoginTests.driver.get(LoginTests.base_url)
        # obj_test2 = lp(LoginTests.driver)
        LoginTests.test_obj.login('bac@email.com', 'abcabc')
        result = LoginTests.test_obj.verifyLoginFailed()
        assert result == True


