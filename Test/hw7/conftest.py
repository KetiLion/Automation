# import selenium, pytest, webdriver_manager, time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# @pytest.fixture(scope="function")
# # декоратор, в скобках выбираем на какой уровень будеть распространятся текстура
# def driver():
#     print("start browser")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     #yield почти тоже самое что и return
#     driver.quit()
#     # посте того как вернули его с помощю yield закрываем его через .quit()
#
#
#
#
