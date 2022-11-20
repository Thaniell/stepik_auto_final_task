from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), \
            "There are products in the basket though they should not be"

    def should_have_products(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TOTAL), \
            "There are no products in the basket though there should be"

    def should_be_empty_message_en(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_EN), \
            "'Your basket is empty' message is not presented"

    def should_not_be_empty_message_en(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_EN), \
            "'Your basket is empty' message is presented though should not be"
