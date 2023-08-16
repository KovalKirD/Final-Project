# Страница Продукта
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_basket(self):  # добавить в корзину
        self.button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        self.button_add_basket.click()

    def match_basket_added_name(self):  # проверка: "Название товара в корзине"
        self.name_added_basket = self.browser.find_element(*ProductPageLocators.NAME_ADDED_BASKET)
        self.name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert self.name_product.text == self.name_added_basket.text, \
            'product name not match basket product name'

    def match_basket_added_price(self):
        self.price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        self.price_added_basket = self.browser.find_element(*ProductPageLocators.PRICE_ADDED_BASKET)
        assert self.price_product.text == self.price_added_basket.text, \
            'product price not match basket product price'