from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        obj_test1 = LoginPage(driver)
        obj_test1.login('test@email.com', 'abcabc')

        # invalid_login_msg = driver.find_element(By.CSS_SELECTOR, '.alert-danger')
        login_check = driver.find_element(By.ID, 'search-courses')
        if login_check is not None:
            print('Test pass, Login is success')
        else:
            print('Test fail, Login is not success')

        driver.close()

    def test_invalidLogin(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        obj_test2 = LoginPage(driver)
        obj_test2.login('bac@email.com', 'abcabc')

        invalid_login_msg = driver.find_element(By.CSS_SELECTOR, '.alert-danger')
        if invalid_login_msg is not None:
            print('Test pass, Login is not success as expected ')
        else:
            print('Test fail, Login is success')

        driver.close()


