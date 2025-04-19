from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

class WebdriverRobot(webdriver.Chrome):
    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(20)
        super().__exit__(exc_type, exc_val, exc_tb)

    def calc(self, value):
        return str(math.log(abs(12 * math.sin(int(value)))))

with WebdriverRobot() as new_window:
    new_window.get(link)
    cost = WebDriverWait(new_window, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    new_window.find_element(By.ID, 'book').click()
    x = new_window.find_element(By.ID, 'input_value').text
    y = new_window.calc(x)
    new_window.find_element(By.ID, 'answer').send_keys(y)
    new_window.find_element(By.ID, 'solve').click()
