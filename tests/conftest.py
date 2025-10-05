import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from data.Checkout_Data import checkout_data

@pytest.fixture(scope="function")
def setup():
    options=Options()

    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.implicitly_wait(5)


    yield driver
    driver.quit()

@pytest.fixture
def formulaire_info():
    return checkout_data.formulaire()