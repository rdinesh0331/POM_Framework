import pytest
from Pytest.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("setup","setupClass")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self,setupClass):
        self.ab =  SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.ab.sum(10,10)
        assert result == 30
        print('Test Method A Running')

    def test_methodB(self):
        result = self.ab.sum(10,20)
        assert result >50
        print('Test Method B Running')
