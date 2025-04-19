from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

class WebdriverRobot(webdriver.Chrome):
    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(20)
        super().__exit__(exc_type, exc_val, exc_tb)

    def calc(self, value):
        return str(math.log(abs(12 * math.sin(int(value)))))

with WebdriverRobot() as new_window:
    new_window.get(link)
    new_window.find_element(By.CLASS_NAME, 'btn').click()
    new_window.switch_to.alert.accept()
    x = new_window.find_element(By.ID, 'input_value').text
    y = new_window.calc(x)
    new_window.find_element(By.ID, 'answer').send_keys(y)
    new_window.find_element(By.CLASS_NAME, 'btn').click()
