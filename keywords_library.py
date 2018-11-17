from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import *
from selenium.webdriver.support import exception_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

class keywords_library:
####################################

    def __init__(self, driver):
        self.driver = driver
        
####################################
    def launch_url(self, url):
        '''
            launch the url
            paramater: URL
            return value: None
        '''
        self.driver.get(url)

####################################
    def verify_title(self, text):
        '''
            verify the title
            paramater: title text to verify
            return value: True or False
        '''        
        text = text.lower()
        captured_title = self.driver.title
        if text == captured_title.lower():
            print('title match - pass, title from the browser is ' + captured_title)
            return True
        else:
            print('title match - fail, title from the browser is ' + captured_title)
            return False

####################################
    
    def getByType(self, locatortype):
        '''
            function to get locator type
            parameter: locator type like ID,XPATH, CSS.. et
            return value: by. ID, by.XPATH..etc
        '''
        locatortype = locatortype.lower()
        if locatortype == 'id':
            return By.ID
        elif locatortype =='xpath':
            return By.XPATH
        elif locatortype=='css':
            return By.CSS_SELECTOR
        elif locatortype == 'name':
            return By.NAME
        elif locatortype == 'linktext':
            return By.LINK_TEXT
        elif locatortype == 'partiallinktext':
            return By.PARTIAL_LINK_TEXT
        elif locatortype =='tagname':
            return By.TAG_NAME
        else:
            print('locator type is invalid')
            return None

####################################
        
    def getElement(self, locator,locatortype='ID'):
        '''
            enter the text in the editbox field
            parameters:  locatortype, locator
            return value: element or None
        '''
        element = None
        try:
            by_value= getByType(locatortype)
            element = self.driver.find_element(by_value, locator)
            print('Element is found')
            return element
        except:
            print('Element is not found')
        return None
            
####################################

    def waitForElement(self, locator, timeout=10, locatortype='ID',poll_frequency=1):
        '''
            Explicit wait
            paramters: locator, locator type, timeout
            return:
        '''
        element = None
        try:
            locatortype= locatortype.lower()
            byType = self.getByType(locatortype)
            wait = WebDriverWait(driver, timeout, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType,locator)))
            print("Element appeared on the web pages")
        except:
            print("Element not appeared on the web pages")
            print_stack()
        return element
    
            
        
        
        

