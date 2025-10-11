from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    def verifier_ouverture_de_la_login_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.champ_password))
    def remplir_le_champ_user(self, text):
        self.remplir_un_champ(self.champ_identifiant, text)

    def remplir_le_champ_pwd(self, text):
        self.remplir_un_champ(self.champ_password, text)

    def cliquer_sur_login(self):
        self.cliquer_sur_element(self.login_button)

    def verifier_la_presence_du_bouton_login(self):
        self.verifier_le_texte_dun_champ(self.login_button)


    def verifier_le_message_erreur_connexion(self):
        message_erreur = self.verifier_le_texte_dun_champ(self.message_erreur_connexion)
        assert "Epic sadface" in message_erreur





