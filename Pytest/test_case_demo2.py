import pytest

@pytest.fixture()
def setup():
    print('Run every demo2 test method starts')
    yield
    print('Run every demo2 test method ends')

def test_methodA(setup):
    print('Print testcase_demo2 method A')

def test_methodB(setup):
    print('Print testcase_demo2 Method B')