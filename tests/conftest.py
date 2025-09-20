# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(base_url):  # fourni par pytest-base-url
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)

    # Ouvre la page de test
    url = base_url or "https://www.saucedemo.com/"
    driver.get(url)

    yield driver
    driver.quit()
