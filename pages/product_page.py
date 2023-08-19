# Страница Продукта
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_basket(self):  # добавить в корзину
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def match_basket_added_name(self):  # проверка: "Название товара в корзине"
        name_added_basket = self.browser.find_element(*ProductPageLocators.NAME_ADDED_BASKET)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert name_product.text == name_added_basket.text, \
            'Product name not match basket product name'

    def match_basket_added_price(self):  # проверка: "Цена товара в корзине"
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_added_basket = self.browser.find_element(*ProductPageLocators.PRICE_ADDED_BASKET)
        assert price_product.text == price_added_basket.text, \
            'Product price not match basket product price'

    def should_not_be_success_message(self):  # проверка: "Успешное сообщение не появилось"
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MASSAGE), \
            'Success message is presented, but should not be'

    def should_is_disappeared_success_message(self):  # проверка: "Элемент исчез"
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE), \
            'Success message is not disappeared, but should is disappeared'