import pytest

@pytest.fixture()
def setUp():
    print('Demo2 Run every test method starts')
    yield
    print('Demo2 Run every test method ends')

def test_demo2_methodA(setUp):
    print('Demo2 MethodA running')


def test_demo2_methodB(setUp):
    print('Demo2 MethodB running')
