from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    brower_name = request.config.getoption("browser_name")
    if brower_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)

    elif brower_name =="firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()