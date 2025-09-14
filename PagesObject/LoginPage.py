from selenium.webdriver.common.by import By
from PagesObject.BasePage import BasePage

class LoginPage(BasePage):


    #locators
    champ_identifiant = (By.ID, "user-name")
    champ_password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    message_erreur_connexion = (By.CSS_SELECTOR, "h3[data-test='error']")


    # méthodes
    def __init__(self, driver):
        super().__init__(driver)
    def remplir_le_champ_user(self, text):
        self.remplir_un_champ(self.champ_identifiant, text)

    def remplir_le_champ_pwd(self, text):
        self.remplir_un_champ(self.champ_password, text)

    def cliquer_sur_login(self):
        self.cliquer_sur_element(self.login_button)

    def verifier_le_message_erreur_connexion(self):
        message_erreur = self.verifier_le_texte_dun_champ(self.message_erreur_connexion)
        assert "Epic sadface" in message_erreur





