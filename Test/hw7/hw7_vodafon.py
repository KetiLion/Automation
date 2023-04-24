import selenium, pytest, webdriver_manager, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def test_open_site():
    driver.get('https://www.vodafone.ua/gold-number#:~:text=%2D%20%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D1%96%D1%82%D1%8C%20%D0%B7%20%D1%86%D1%96%D1%94%D1%97%20%D0%B6%20SIM,%D0%BD%D0%BE%D0%BC%D0%B5%D1%80%2C%20%D0%BE%D0%B1%D1%80%D0%B0%D0%BD%D0%B8%D0%B9%20%D0%92%D0%B0%D0%BC%D0%B8%20%D0%BD%D0%B0%20%D1%81%D0%B0%D0%B9%D1%82%D1%96')
    # driver.maximize_window()
    # assert 'vodafone' in driver.current_url
    # print(driver.current_url)

def test_site_check_title():
    assert driver.title == 'Вибір номера — Золоті номери Vodafone'

def test_input_find_number():
    search_number_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='XXX-XX-XX']")
    search_number_field.send_keys('999832')
    time.sleep(5)
    push_button = driver.find_element(By.CSS_SELECTOR, '.submit-btn.active')
    push_button.click()
    time.sleep(5)
