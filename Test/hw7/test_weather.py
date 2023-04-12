# install selenium in terminal or "local" $ pip3 install selenium
# $ pip3 install pytest
# $ pip3 install webdriver-manager || pip3 install webdriver_manager
import selenium, pytest, webdriver_manager, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# это нужно чтобы взаимодействовать с браузером

def test_is_SELENIUM_installed_and_what_version():
    """
    Function requires "import selenium" + #pip3 install selenium
    Function checks if the project has Selenium installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Selenium" installed successfully;
    2. "Selenium" imported successfully;
    3. "Selenium" version is = 4.8.3 "
    """
    print('\n1. "Selenium" installed successfully; \n'
          '2. "Selenium" imported successfully;  \n'
          '3. "Selenium" version is =', selenium.__version__, '\n')
test_is_SELENIUM_installed_and_what_version()

def test_is_PYTEST_installed_and_what_version():
    """
    Function requires "import pytest" + #pip3 install pytest
    Function checks if the project has Pytest installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Pytest" installed successfully;
    2. "Pytest" imported successfully;
    3. "Pytest" version is = 7.2.2 "
    """
    print('\n1. "Pytest" installed successfully; \n'
          '2. "Pytest" imported successfully;  \n'
          '3. "Pytest" version is =', pytest.__version__, '\n')
test_is_PYTEST_installed_and_what_version()

def test_is_WEBDRIVER_MANAGER_installed_and_what_version():
    """
    Function requires "import webdriver_manager" + #pip3 install webdriver_manager (#pip3 install webdriver-manager)
    Function checks if the project has Webdriver_manager installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Webdriver_manager" installed successfully;
    2. "Webdriver_manager" imported successfully;
    3. "Webdriver_manager" version is = 3.8.5 "
    """
    print('\n1. "Webdriver_manager" installed successfully; \n'
          '2. "Webdriver_manager" imported successfully;  \n'
          '3. "Webdriver_manager" version is =', webdriver_manager.__version__, '\n')
test_is_WEBDRIVER_MANAGER_installed_and_what_version()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
## тут мы указываем чтобы он находил последнюю версию браузера и устанавливал ее

def test_open_site():
    driver.get('https://openweathermap.org/')
    # открывает страницу
    driver.maximize_window()
    # открывает страницу на полный экран
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)

def test_site_title_txt():
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_input_find_city():
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Search city']")
    # вложенные кавычки должны быть не такими как внешние
    search_city_field.send_keys('New York')
    # набирает текст в search_city_field   >>>>   'input[placeholder="Search city"]'
    time.sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # находит указанную кноку
    search_button.click()
    time.sleep(5)
    drop_down_menu_first_item = driver.find_element(By.CSS_SELECTOR, "div[class='grey-container'] li:nth-child(1) span:nth-child(1)")
    drop_down_menu_first_item.click()
    time.sleep(5)
    expected_city = 'New York'
    displayed_city = driver.find_element(By.CSS_SELECTOR, "div[class='current-container mobile-padding'] div h2")
    displayed_city_text = displayed_city.text
    # вытащить с элемента текст .text
    print('"' + expected_city + '" is in "' + displayed_city_text + '"')
    assert expected_city in displayed_city_text

