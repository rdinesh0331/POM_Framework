import pytest

@pytest.fixture()
def setup():
    print('Conftest method setup running')
    yield
    print('Conftest method teardown running')

@pytest.fixture(scope='class')
def setupClass(request, browserType,OSType):
    print('Conftest class setup running')
    if browserType =='firefox':
        print('Running on firefox')
        value = 20
    else:
        print('Running on Chrome')
        value = 10
    if request.cls is not None:
        request.cls.value = value
    yield value

    print('Conftest class teardown running')

def pytest_addoption(parser):
    parser.addoption('--browserType')
    parser.addoption('--OStype', help='Type of Operating system')

@pytest.fixture(scope = 'session')
def browserType(request):
    return request.config.getoption('--browserType')

@pytest.fixture(scope = 'session')
def OStype(request):
    return request.config.getoption('--OStype')






