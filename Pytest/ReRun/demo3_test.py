import pytest

@pytest.fixture()
def setUp():
    print('Demo3 Run every test method starts')
    yield
    print('Demo3 Run every test method ends')

def test_demo3_methodA(setUp):
    print('Demo3 MethodA running')


def test_demo3_methodB(setUp):
    print('Demo3 MethodBrunning')
