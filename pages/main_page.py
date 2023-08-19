# Главная Страница
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):  # заглушка pass
        super(MainPage, self).__init__(*args, **kwargs)