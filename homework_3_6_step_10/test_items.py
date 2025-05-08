from selenium.webdriver.common.by import By
import time

class TestShopItems:

    def test_buy_button_exists(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(10)

        #добавляем немного информации в лог
        page_language_list = browser.find_element(By.CSS_SELECTOR, "[selected='selected']")
        page_language = page_language_list.text
        print(f'\npage language is {page_language}')

        #проверяем, что страница товара содержит кнопку добавления в корзину
        buy_button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        assert buy_button, f'There is no "Add to basket" button on the "{page_language}" page'
