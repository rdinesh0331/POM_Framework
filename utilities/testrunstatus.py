import logging
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_log


class TestRunStatus(SeleniumDriver):

    log= custom_log(logging.INFO)

    def __init__(self,driver):
        super().__init__(driver)
        self.resultlist=[]


    def setResult(self,result,resultMessage):

        try:

            if result is not None:
                if result:
                    self.resultlist.append('PASS')
                    self.log.info('### VERIFICATION SUCCESS')
                else:
                    self.resultlist.append('FAIL')
                    self.log.info('### VERIFICATION FAILED '+resultMessage)
            else:
                self.resultlist.append('FAIL')
                self.log.info('### VERIFICATION FAILED ' + resultMessage)

        except:
            self.resultlist.append('FAIL')
            self.log.info('### EXCEPTION OCCURED!!!')


    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)


    def markFinal(self,testcase, result, resultMessage):
        self.setResult(result,resultMessage)
        if 'FAIL' in self.resultlist:
            self.log.error(testcase + '### TEST FAILED')
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testcase + '### TEST PASSED')
            self.resultlist.clear()
            assert True == True

