import pytest

@pytest.fixture()
def setup():
    print('Run every conftest demo test method starts')
    yield
    print('Run every conftest demo test method ends')


@pytest.fixture(scope ="class")
def setupClass(request, browser,OSType):
    print('Run every conftest class starts')
    if browser == 'firefox':
        print('Running the tests on FireFox')
        value = 20
    else:
        print('Running the tests on Chrome')
        value =10

    if request.cls is not None:
        request.cls.value = value

    yield value
    print('Run every conftest class ends')


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OSType", help='Type of operating system')

@pytest.fixture(scope = 'session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def OSType(request):
    return request.config.getoption('--OSType')