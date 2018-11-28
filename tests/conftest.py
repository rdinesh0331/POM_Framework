import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setup(onetime_Setup):
    print('Running setup at method level')
    yield
    print('Running teardown at method level')


@pytest.fixture(scope='class')
def onetime_Setup(request,BrowserOption,OStype):
    print('Running onetimeSetup')
    wdf = WebDriverFactory(BrowserOption)
    driver = wdf.getDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

    print('Teardown onetimeSetup')

def pytest_addoption(parser):
    parser.addoption('--BrowserOption')
    parser.addoption('--OStype')

@pytest.fixture(scope='session')
def BrowserOption(request):
    return request.config.getoption('--BrowserOption')


@pytest.fixture(scope='session')
def OStype(request):
    return request.config.getoption('--OStype')