from selenium.webdriver.common.by import By
import time

class TestShopItems:

    def test_buy_button_exists(self, browser, language):
        #создаем список разрешенных языков и проверяем, входит ли переданное значение в этот список
        allowed_languages = ['en-gb', 'es', 'fr', 'ar', 'ca', 'cs', 'da', 'de', 'el', 'fi', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-cn']
        assert language in allowed_languages, f'{language} is not allowed language'

        #получаем список страницы с указанным языком и переходим по ней
        link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(10)

        #добавляем немного информации в лог
        print(f'\nchosen language is {language}')
        page_language_list = browser.find_element(By.CSS_SELECTOR, "[selected='selected']")
        page_language = page_language_list.text
        print(f'page language is {page_language}')

        #проверяем, что страница товара содержит кнопку добавления в корзину
        buy_button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        assert buy_button, f'There is no "Add to basket" button on the "{page_language}" page'
