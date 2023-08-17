# Тесты Продуктовых Страниц
import time
import pytest
from pages.product_page import ProductPage

offer_number = [n for n in range(10)]
@pytest.mark.parametrize('offer', offer_number)
def test_guest_can_add_product_to_basket(browser, offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'
    page = ProductPage(browser, link)  # инициализируем объект страницу
    page.open()                        # открываем страницу
    page.add_basket()                  # добавляем товар в корзину
    page.solve_quiz_and_get_code()     # вводим код в allert
    page.match_basket_added_name()     # проверяем название товара с товаром в корзине
    page.match_basket_added_price()    # проверяем цену товара с ценой в корзине

@pytest.mark.skip
@pytest.mark.success_message
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_basket()
    page.should_not_be_success_message()

@pytest.mark.success_message
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.success_message
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_basket()
    page.should_is_disappeared_success_message()
