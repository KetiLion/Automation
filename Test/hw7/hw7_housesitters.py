# import selenium, pytest, webdriver_manager, time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# def test_open_site():
#     driver.get('https://www.trustedhousesitters.com/')
#     assert 'trustedhousesitters' in driver.current_url
#
# def test_login():
#     search_login = driver.find_element(By.XPATH, "//a[@class='sc-g5xyr8-1 ifIJAc']")
#     search_login.click()
#     time.sleep(5)
#     email_address_login = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address']")
#     email_address_login.send_keys('________@gmail.com')
#     time.sleep(5)
#     password_address_login = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
#     password_address_login.send_keys('*****')
#     time.sleep(5)
#     button_login = driver.find_element (By.CSS_SELECTOR, "button[button-type='primary']")
#     button_login.click()
#     time.sleep(5)
