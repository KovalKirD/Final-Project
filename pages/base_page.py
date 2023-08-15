# Базовая Страница|Базовые методы управления
import math
from selenium.common import NoSuchElementException
from selenium.common import NoAlertPresentException

class BasePage:
    def __init__(self, browser, url, timeout=10):  # конструктор класса
        self.browser = browser                 # назначить браузер
        self.url = url                         # присвоить ссылку
        self.browser.implicitly_wait(timeout)  # неявное ожидание элемента

    def open(self):  # открывает страницу
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # перехватчик исключений
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
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