# Главная Страница|Методы тестов
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):  # перейти на страницу авторизации
        self.login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        self.login_link.click()

    def should_be_login_link(self):  # проверить ссылку на логин
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'