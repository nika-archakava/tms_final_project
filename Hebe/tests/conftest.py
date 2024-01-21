import allure
import pytest
from selenium import webdriver

from Hebe.source_code.pages.main.main_page import MainPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-geolocation')
    options.add_argument('--disable-notifications')
    options.add_argument('--window-size=1920,1080')
    with webdriver.Chrome(options) as driver:
        yield driver


@pytest.fixture(autouse=True)
@allure.step('Open main page')
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.driver.get('https://www.hebe.pl/')
