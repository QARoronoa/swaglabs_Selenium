from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.BasePage import BasePage

class HomePage(BasePage):



    #locator
    titre_page_dacceuil = (By.CSS_SELECTOR, ".product_label")
    bouton_add_to_cart_article_1 = (By.XPATH, "(//button[text()='ADD TO CART'])[1]")
    cart_badge = (By.CSS_SELECTOR, ".fa-layers-counter")
    remove_button = (By.XPATH, "//button[text()='REMOVE']")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)


    def verifier_la_redirection_vers_homePage(self):
        titre_Products = self.verifier_le_texte_dun_champ(self.titre_page_dacceuil)
        assert titre_Products == "Products"

    def cliquer_sur_add_to_cart_Sauce_Labs_Backpack(self):
        self.cliquer_sur_element(self.bouton_add_to_cart_article_1)

    def verifier_la_quantite_affiche_sur_badge_panier(self, text):
        quantite_panier = self.verifier_le_texte_dun_champ(self.cart_badge)
        assert quantite_panier == text

    def cliquer_sur_le_bouton_remove(self):
        self.cliquer_sur_element(self.remove_button)
        badge_cart = (WebDriverWait(self.driver, 10).until
                      (EC.invisibility_of_element_located(self.cart_badge)))
