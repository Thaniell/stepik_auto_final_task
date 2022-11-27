from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link_the_city = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'fKs'
        page.register_new_user(email, password)
        browser.implicitly_wait(5)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, link_the_city)
        page.open()
        page.should_not_be_success_message()
        # Открываем страницу товара
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, link_the_city)
        page.open()
        page.add_to_basket()
        page.should_be_product_name()
        page.should_be_product_price()


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.should_not_be_success_message()
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear()
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_the_city)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link_the_city)
    basket_page.should_not_have_products()
    basket_page.should_be_empty_message_en()
    # Гость открывает страницу товара
    # Переходит в корзину по кнопке в шапке
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
