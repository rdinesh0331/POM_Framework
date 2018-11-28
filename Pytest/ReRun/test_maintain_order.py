import pytest

@pytest.mark.run(order=1)
def test_conftest_OrderDemo_MethodA(setupClass,setup):
    print('OrderDemo test_conftest_MethodA')

def test_conftest_OrderDemo_MethodB(setupClass,setup):
    print('OrderDemo_test_conftest_MethodB')

@pytest.mark.run(order=2)
def test_conftest_OrderDemo_MethodC(setupClass,setup):
    print('OrderDemo test_conftest_MethodC')

@pytest.mark.run(order=3)
def test_conftest_OrderDemo_MethodD(setupClass,setup):
    print('OrderDemo_test_conftest_MethodD')