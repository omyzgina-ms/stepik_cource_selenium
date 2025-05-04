from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    FIELD_EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    FIELD_CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-success div.alertinner strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-info div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')

class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, 'div.content>div#content_inner>p')
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, 'form#basket_formset')