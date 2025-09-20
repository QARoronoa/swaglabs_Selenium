import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def setup():
    options = Options()
    options.add_argument("-headless")  # indispensable en CI
    # NE PAS définir options.binary_location (laisse Selenium Manager trouver firefox)
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
