# Страница Продукта
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_basket(self):
        self.button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        self.button_add_basket.click()

    def should_be_basket_added_name(self):
        self.basket_added_name = self.browser.find_element()
        assert 