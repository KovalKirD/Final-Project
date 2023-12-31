# Базовая Страница|Базовые методы управления
import math
from selenium.common import NoSuchElementException
from selenium.common import NoAlertPresentException
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):  # конструктор класса
        self.browser = browser                 # назначить браузер
        self.url = url                         # присвоить ссылку
        self.browser.implicitly_wait(timeout)  # неявное ожидание элемента

    def open(self):  # открыть страницу
        self.browser.get(self.url)

    def go_to_login_page(self):  # перейти на страницу авторизации
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):  # перейти в корзину
        view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        view_basket.click()

    def should_be_authorized_user(self):  # проверка, что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):  # проверить ссылку на логин
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def is_element_present(self, how, what):  # перехватчик исключений: элемент представлен
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # перехватчик исключений: элемент отсутствует
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):  # перехватчик исключений: элемент исчез
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):  # получение проверочного кода в alert
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")