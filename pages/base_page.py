# Базовая Страница
class BasePage:
    def __init__(self, browser, url):  # конструктор класса
        self.browser = browser
        self.url = url

    def open(self):  # открывает страницу
        self.browser.get(self.url)