import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestUnittest(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
            input1.send_keys("TestName")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
            input2.send_keys("TestSurname")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
            input3.send_keys("TestEmail")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(first="Congratulations! You have successfully registered!", second=welcome_text, msg='Registration is not successful')

        finally:
            time.sleep(10)
            browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
            input1.send_keys("TestName")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
            input2.send_keys("TestSurname")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
            input3.send_keys("TestEmail")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(first="Congratulations! You have successfully registered!", second=welcome_text, msg='Registration is not successful')

        finally:
            time.sleep(10)
            browser.quit()