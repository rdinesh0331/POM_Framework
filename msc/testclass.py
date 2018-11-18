from msc.keywords_library import *


class testclass:
    
    def test_method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver
1
2
3
import logging
log = logging.getLogger("my-logger")
log.info("Hello, world").implicitly_wait(7)
        s = keywords_library(driver)
        s.launch_url('https://learn.letskodeit.com/p/practice')
        if s.verify_title("Practice | Let's Kode It") is False:
            return 'Fail'
        

t = testclass()
t.test_method()
        
        
        
