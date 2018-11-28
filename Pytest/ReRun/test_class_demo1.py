import pytest
from Pytest.ReRun.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("setupClass","setup")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.obj = SomeClassToTest(10)

    def test_methodA(self):
        print('Running methodA')
        result = self.obj.sumNo(10,10)
        assert result == 30

    def test_methodB(self):
        print('Running methodB')
        result = self.obj.sumNo(20,20)
        assert result >= 30
