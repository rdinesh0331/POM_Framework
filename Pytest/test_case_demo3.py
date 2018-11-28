import pytest

@pytest.fixture()
def setup():
    print('Run every demo3 test method starts')
    yield
    print('Run every demo3 test method ends')

def test_methodA(setup):
    print('Print testcase demo3 method A')

def test_methodB(setup):
    print('Print testcase demo3 Method B')