from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.BasePage import BasePage

class HomePage(BasePage):



    #locator
    titre_page_dacceuil = (By.CSS_SELECTOR, ".product_label")
    bouton_add_to_cart_article_1 = (By.XPATH, "(//button[text()='ADD TO CART'])[1]")
    bouton_add_to_cart_article_3= (By.XPATH, "(// button[text() = 'ADD TO CART'])[3]")
    cart_badge = (By.CSS_SELECTOR, ".fa-layers-counter")
    remove_button = (By.XPATH, "//button[text()='REMOVE']")
    bouton_panier = (By.CSS_SELECTOR, ".shopping_cart_link")
    bouton_burger=(By.CSS_SELECTOR, ".bm-burger-button")
    bouton_logout = (By.ID, "logout_sidebar_link")
    titre_item_labs_backPack = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    image_sauce_labs_backpack = (By.XPATH, "(//div[@class='inventory_item_img'])[1]")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)


    def verifier_la_redirection_vers_homePage(self):
        titre_Products = self.verifier_le_texte_dun_champ(self.titre_page_dacceuil)
        assert titre_Products == "Products"

    def cliquer_sur_add_to_cart_Sauce_Labs_Backpack(self):
        self.cliquer_sur_element(self.bouton_add_to_cart_article_1)

    def cliquer_sur_add_to_cart_Sauce_Labs_Bolt_T_Shirt(self):
        self.cliquer_sur_element(self.bouton_add_to_cart_article_3)

    def verifier_la_quantite_affiche_sur_badge_panier(self, text):
        quantite_panier = self.verifier_le_texte_dun_champ(self.cart_badge)
        assert quantite_panier == text

    def cliquer_sur_le_bouton_remove(self):
        self.cliquer_sur_element(self.remove_button)
        badge_cart = (WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.cart_badge)))

    def cliquer_sur_le_panier(self):
        self.cliquer_sur_element(self.bouton_panier)

    def cliquer_sur_le_bouton_burger(self):
        self.cliquer_sur_element(self.bouton_burger)

    def cliquer_sur_le_bouton_logout(self):
        self.cliquer_sur_element(self.bouton_logout)

    def verifier_nombre_de_produits(self):
        articles = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".inventory_item")))
        nombre_articles = len(articles)
        assert nombre_articles == 6

    def cliquer_sur_sauce_labs_backpack(self):
        self.cliquer_sur_element(self.titre_item_labs_backPack)

    def cliquer_sur_image_sauce_labs_backpack(self):
        self.cliquer_sur_element(self.image_sauce_labs_backpack)
