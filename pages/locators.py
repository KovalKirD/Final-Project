# Локаторы
from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')  # кнопка: "Добавить в Корзину"
    NAME_ADDED_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')  # название: "Товар добавленный в козину"
    NAME_PRODUCT = (By.CSS_SELECTOR,'div.col-sm-6.product_main > h1')  # название: "Товар"
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main > p.price_color')  # текст: цена товара
    PRICE_ADDED_BASKET = (By.CSS_SELECTOR, '.in > div > p:nth-child(1) > strong')  # текст: цена товара добаленного в корзину
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')  # элемент: успешное сообщение