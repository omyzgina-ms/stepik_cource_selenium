from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage:
    @staticmethod
    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def test_guest_can_go_to_login_page(self, browser):
        browser.get(link)
        self.go_to_login_page(browser)
        time.sleep(10)

