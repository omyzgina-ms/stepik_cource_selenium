from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

class WebdriverRobot(webdriver.Chrome):
    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(20)
        super().__exit__(exc_type, exc_val, exc_tb)


def button_click_send(rule, value):
        new_window.find_element(rule, value).click()


with WebdriverRobot() as new_window:
    new_window.get(link)
    res_num = int(new_window.find_element(By.ID, 'num1').text) + int(new_window.find_element(By.ID, 'num2').text)
    sel = Select(new_window.find_element(By.TAG_NAME, 'select'))
    sel.select_by_visible_text(str(res_num))
    button_click(By.CSS_SELECTOR, 'button.btn')


# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     elem_x = browser.find_element(By.ID, 'treasure')
#     x = elem_x.get_attribute('valuex')
#     y = calc(x)
#
#     browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
#     browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
#     browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
#
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла