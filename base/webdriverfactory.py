from selenium import webdriver

class WebDriverFactory():

    def __init__(self,browser):
        self.browser = browser.lower()



    def getDriverInstance(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        if self.browser=='ie':
            driver = webdriver.Ie()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        return driver
