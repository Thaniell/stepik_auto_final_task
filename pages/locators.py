from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CLASS_NAME, 'icon-user')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.NAME, 'registration-password2')
    REGISTER = (By.NAME, 'registration_submit')

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CLASS_NAME,'product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '#messages .alert-info .alertinner strong')

class  BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, 'th.total h3')
    BASKET_IS_EMPTY_EN = (By.CSS_SELECTOR, '#content_inner p')


