from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem_x = browser.find_element(By.ID, 'input_value')
    y = calc(elem_x.text)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла