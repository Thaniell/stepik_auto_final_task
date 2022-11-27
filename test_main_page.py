from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


link_main = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link_main)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link_main)
        page.open()
        page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, link_main)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link_main)
    basket_page.should_not_have_products()
    basket_page.should_be_empty_message_en()
    # basket_page.should_have_products()
    # basket_page.should_not_be_empty_message_en()
    # Гость открывает главную страницу
    # Переходит в корзину по кнопке в шапке сайта
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
