# Тесты Продуктовых Страниц
import time
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)  # инициализируем объект страницу
    page.open()                        # открываем страницу
    page.add_basket()                  # добавляем товар в корзину
    page.solve_quiz_and_get_code()     # вводим код в allert
    page.match_basket_added_name()     # проверяем название товара с товаром в корзине
    page.match_basket_added_price()    # проверяем цену товара с ценой в корзине