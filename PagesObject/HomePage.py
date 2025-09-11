from selenium.webdriver.common.by import By

from PagesObject.BasePage import BasePage

class HomePage(BasePage):



    #locator
    titre_page_dacceuil = (By.CSS_SELECTOR, ".product_label")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)


    def verifier_la_redirection_vers_homePage(self):
        titre_Products = self.verifier_le_texte_dun_champ(self.titre_page_dacceuil)
        assert titre_Products == "Products"