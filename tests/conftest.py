import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def setup():
    options=Options()

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.implicitly_wait(5)


    yield driver
    driver.quit()