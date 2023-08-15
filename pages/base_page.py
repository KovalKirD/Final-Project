# Базовая Страница|Базовые методы управления
from selenium.common import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):  # конструктор класса
        self.browser = browser  # назначить браузер
        self.url = url          # присвоить ссылку
        self.browser.implicitly_wait(timeout)  # неявное ожидание элемента

    def open(self):  # открывает страницу
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # перехватчик исключений
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True