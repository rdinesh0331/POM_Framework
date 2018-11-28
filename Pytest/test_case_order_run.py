import pytest


@pytest.mark.last
# @pytest.mark.run(order=1)
def test_methodA(setup, setupClass):
    print('Print testcase demo4 method A')

@pytest.mark.run(order=1)
def test_methodB(setup, setupClass):
    print('Print testcase demo4 Method B')

@pytest.mark.first
# @pytest.mark.run(order=2)
def test_methodC(setup, setupClass):
    print('Print testcase demo4 Method C')

@pytest.mark.second
def test_methodD(setup, setupClass):
    print('Print testcase demo4 Method D')

# @pytest.mark.run(order=3)
def test_methodE(setup, setupClass):
    print('Print testcase demo4 Method E')