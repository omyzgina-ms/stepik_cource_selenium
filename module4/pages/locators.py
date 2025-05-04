from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-success div.alertinner strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-info div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')