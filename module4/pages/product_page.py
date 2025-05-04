from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def buy_product(self):
        buy_button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_button.click()

    def should_be_purchase_confirmation(self):
        product_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        assert product_in_basket.text == product_on_page.text, f'Product in the basket does not match the product on the page. Got "{product_in_basket.text}" instead of "{product_on_page.text}"'

    def should_be_basket_price(self):
        price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert price_on_page.text == price_in_basket.text, f'Price in the basket does not match the price on the page. Got "{price_in_basket.text}" instead of "{price_on_page.text}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_not_be_element(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but they should disappear'
