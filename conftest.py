# Конфигурация тестов
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):  # обработчик опции language
    parser.addoption('--language', action='store', default='user_language',
                     help='Choose language: ru, es, us')  # пример --language=es

@pytest.fixture(scope='function')  # фикстура запуска/закрытия браузера
def browser(request):
    language = request.config.getoption('language')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print('\nstart browser for test...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser')
    browser.quit()