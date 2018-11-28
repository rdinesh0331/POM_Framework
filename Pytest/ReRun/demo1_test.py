import pytest

@pytest.fixture()
def setUp():
    print('Demo1 Run every test method starts')

def test_demo1_methodA(setUp):
    print('Demo1 MethodA running')


def test_demo1_methodB(setUp):
    print('Demo1 MethodB running')
