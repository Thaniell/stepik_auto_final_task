from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), \
            "Success message is presented, but should not be"

    def should_be_empty_en(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_EN), \
            "'Your basket is empty' message is not presented"
