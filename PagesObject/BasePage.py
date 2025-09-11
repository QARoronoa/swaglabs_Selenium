from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def cliquer_sur_element(self, locator):
        element = WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.click()

    def remplir_un_champ(self, locator, text):
        element = WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return element.text

    def verifier_le_texte_dun_champ(self, locator):
        element = WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text