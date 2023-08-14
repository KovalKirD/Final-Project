# Главная Страница
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):  # перейти на страницу авторизации
        self.login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        self.login_link.click()

    def should_be_login_link(self):  # проверить ссылку на логин
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")