import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose preferable language: en-gb, es, fr or ru")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('--language')

    # создаем список разрешенных языков и проверяем, входит ли переданное значение в этот список
    allowed_languages = ['en-gb', 'es', 'fr', 'ar', 'ca', 'cs', 'da', 'de', 'el', 'fi', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-cn']
    assert language in allowed_languages, f'{language} is not allowed language'

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()