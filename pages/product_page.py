from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_link.click()

    def should_be_product_name(self):
        p_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        m_product_in_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert m_product_in_basket == f'{p_name} has been added to your basket.', "The name of the added product " \
                                                                                  "does not match the page's product "

    def should_be_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert price == total, "The price does not match the basket total"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message didn't disappear"
