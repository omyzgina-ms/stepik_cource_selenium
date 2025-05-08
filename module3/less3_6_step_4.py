import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

import secrets_stepik
from stepik_cource_selenium.module3.conftest import browser


class TestAuth:

    @pytest.fixture(scope='class')
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.fixture
    def answer(self):
        answer = math.log(int(time.time()))
        return answer

    @pytest.mark.parametrize('page_link',
                             ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                              'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                              'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                              'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
    def test_stepik_authorised(self, browser, page_link, answer):
        browser.get(page_link)
        time.sleep(15)
        auth_link = browser.find_elements(By.CSS_SELECTOR, 'a.navbar__auth_login')
        if auth_link:
            browser.find_element(By.CSS_SELECTOR, 'a.navbar__auth_login').click()
            browser.find_element(By.ID, 'id_login_email').send_keys(secrets_stepik.stepik_login)
            browser.find_element(By.ID, 'id_login_password').send_keys(secrets_stepik.stepik_pass)
            browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
            browser.get(page_link)
        else:
            task_text = WebDriverWait(browser, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.string-quiz__textarea')))
            browser.find_element(By.CSS_SELECTOR, 'textarea.string-quiz__textarea').send_keys(str(answer))
            browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
            optional_feedback = WebDriverWait(browser, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint')))
            assert optional_feedback.text == 'Correct!', f'Expected "Correct!", got instead {optional_feedback.text}'



    # @pytest.mark.parametrize('page_link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
    # def test_get_feedback(self, answer, browser, page_link):
    #     browser.get(page_link)
    #     task_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.string-quiz__textarea')))
    #     browser.find_element(By.CSS_SELECTOR, 'textarea.string-quiz__textarea').send_keys(str(answer))
    #     browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    #     optional_feedback = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint')))
    #     assert optional_feedback.text == 'Correct!', f'Expected "Correct!", got instead {optional_feedback.text}'