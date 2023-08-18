# Страница Корзины
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_massage(self):  # Ожидаем, что есть текст о том что корзина пуста
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)

    def should_not_be_items_in_basket(self):  # Ожидаем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ITEMS_BY_BASKET)