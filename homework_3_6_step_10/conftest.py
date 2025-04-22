import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose preferable language: en-gb, es, fr or ru")

@pytest.fixture
def language(request):
    return request.config.getoption('--language')

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()