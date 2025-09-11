import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup():
    options=Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")

    yield driver
    driver.quit()