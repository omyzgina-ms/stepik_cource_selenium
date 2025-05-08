# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

#-------------------------------

# import pytest
#
#
# @pytest.fixture(scope="class")
# def prepare_faces():
#     print("^_^", "\n")
#     yield
#     print(":3", "\n")
#
#
# @pytest.fixture()
# def very_important_fixture():
#     print(":)", "\n")
#
#
# @pytest.fixture(autouse=True)
# def print_smiling_faces():
#     print(":-Р", "\n")
#
#
# class TestPrintSmilingFaces():
#     def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
#         print('i')
#
#     def test_second_smiling_faces(self, prepare_faces):
#         print('i')

#-------------------------------

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     @pytest.mark.regression
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#-------------------------------
#
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

#-------------------------------

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

#-------------------------------

# from selenium import webdriver
#
# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Firefox()
#
# driver.get("https://stepik.org/lesson/25969/step/8")

#---------------------------------

from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

#------------------------------------
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")