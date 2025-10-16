from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.BasePage import BasePage


class DetailArticlePage(BasePage):

    #locators
        titre_fiche_produit = (By.CSS_SELECTOR, ".inventory_details_name")
        bouton_back = (By.CSS_SELECTOR, ".inventory_details_back_button")


    #methodes
        def __init__(self, driver):
            super().__init__(driver)

        def verifier_la_redirection_vers_la_fiche_produit(self, article):
            titre_item = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.titre_fiche_produit)).text
            assert titre_item == article, (f"erreur redirection : attendu '{article}', obtenu: {titre_item}")

        def cliquer_sur_bouton_back(self):
            self.cliquer_sur_element(self.bouton_back)