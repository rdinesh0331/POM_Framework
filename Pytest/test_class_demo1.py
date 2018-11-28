import pytest
from Pytest.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("setup","setupClass")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ab =  SomeClassToTest(10)

    def test_methodA(self):
        result = self.ab.sum(10,10)
        assert result == 3
        print('Test Method A Running')

    def test_methodB(self):
        print('Test Method B Running')
