from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

class WebdriverRobot(webdriver.Chrome):
    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(20)
        super().__exit__(exc_type, exc_val, exc_tb)

with WebdriverRobot() as new_window:
    new_window.get(link)
    new_window.find_element(By.NAME, 'firstname').send_keys('Nametest')
    new_window.find_element(By.NAME, 'lastname').send_keys('Lastnametest')
    new_window.find_element(By.NAME, 'email').send_keys('test@mail.com')
    new_window.find_element(By.ID, 'file').send_keys(file_path)
    new_window.find_element(By.CLASS_NAME, 'btn').click()