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
            'Product name not match basket product name'

    def match_basket_added_price(self):  # проверка: "Цена товара в корзине"
        self.price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        self.price_added_basket = self.browser.find_element(*ProductPageLocators.PRICE_ADDED_BASKET)
        assert self.price_product.text == self.price_added_basket.text, \
            'Product price not match basket product price'

    def should_not_be_success_message(self):  # проверка: "Успешное сообщение"
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MASSAGE), \
            'Success message is presented, but should not be'

    def should_is_disappeared_success_message(self):  # проверка: "Элемент исчез"
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE), \
            'Success message is not disappeared, but should is disappeared'