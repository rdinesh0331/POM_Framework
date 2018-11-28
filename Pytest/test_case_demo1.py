import pytest

@pytest.fixture()
def setup():
    print('Run every demo1 test method starts')

def test_methodA(setup):
    print('Print testcase_demo1 method A')

def test_methodB(setup):
    print('Print testcase_demo1 Method B')

def teardown():
    print('Run every demo1 test method stops')