# Страница Авторизации/Регистрации
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):  # общая проверка страницы
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):  # регистрация нового пользователя
        v_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        v_email.send_keys(email)
        v_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        v_password.send_keys(password)
        v_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        v_password_confirm.send_keys(password)
        v_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        v_button.click()

    def should_be_login_url(self):  # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, '"login" not in URL'

    def should_be_login_form(self):  # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login Form not presented'

    def should_be_register_form(self):  # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register Form not presented'