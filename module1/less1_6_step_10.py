from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # req_elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    # for element in req_elements:
    #     element.send_keys()

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
    input1.send_keys("TestName")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input2.send_keys("TestSurname")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input3.send_keys("TestEmail")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Something went wrong'

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла