from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pytest

@pytest.fixture(scope="function")
def setup():
    opts = Options()
    opts.add_argument("-headless")
    driver = webdriver.Firefox(options=opts, service=Service())
    yield driver
    driver.quit()
