from selenium import webdriver
from pages.home.login_page import LoginPage as lp
import unittest
from utilities.custom_logger import custom_log
import logging
import pytest
import time
from utilities.testrunstatus import TestRunStatus as ts


@pytest.mark.usefixtures("onetime_Setup","setup")
class LoginTests(unittest.TestCase):

    # log = custom_log(logging.INFO)

    @pytest.fixture(autouse=True)
    def ClassLevelSetup(self,onetime_Setup):
        self.test_obj = lp(self.driver)
        self.test_status = ts(self.driver)

    @pytest.fixture()
    def setup(self,onetime_Setup):
        base_url = 'https://learn.letskodeit.com/p/practice'
        self.driver.get(base_url)

    # @pytest.mark.skip
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.test_obj.login('test@email.com', 'abcabc')
        result1 = self.test_obj.verify_title("Lets Kode It")
        self.test_status.mark(result1,'title mismatch')
        result2 = self.test_obj.verifyLoginSuccess()
        self.test_status.markFinal('Valid login check', result2, 'Login was not successful')

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        # obj_test2 = lp(LoginTests.driver)
        self.test_obj.login('bac@email.com', 'abcabc')
        result = self.test_obj.verifyLoginFailed()
        self.test_status.markFinal('Invalid login check', result, 'Login was successful')

