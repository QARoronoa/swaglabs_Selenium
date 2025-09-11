from selenium.webdriver.common.by import By
from PagesObject.BasePage import BasePage

class LoginPage(BasePage):


    #locators
    champ_identifiant = (By.ID, "user-name")
    champ_password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    # méthodes
    def __init__(self, driver):
        super().__init__(driver)
    def remplir_le_champ_user(self):
        self.remplir_un_champ(self.champ_identifiant, "standard_user")

    def remplir_le_champ_pwd(self):
        self.remplir_un_champ(self.champ_password, "secret_sauce")

    def cliquer_sur_login(self):
        self.cliquer_sur_element(self.login_button)



