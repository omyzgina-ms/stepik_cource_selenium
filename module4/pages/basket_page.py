from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_messages_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), f'There is no message that basket is empty'

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_presented(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Products are presented in the basket, but they should not'
