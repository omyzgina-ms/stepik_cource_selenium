from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert '/accounts/login/' in current_url, f'Wrong login url! Got {current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), 'Login Form is not presented!'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration Form is not presented!'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.FIELD_EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_CONFIRMATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()