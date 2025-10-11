from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PagesObject.BasePage import BasePage


class CartPAge(BasePage):



    #locators
        titre_cart_page = (By.CSS_SELECTOR, ".subheader")
        checkout_bouton = (By.XPATH, "//a[text()='CHECKOUT']")
        cart_quantity = (By.CSS_SELECTOR, ".cart_quantity")



    # méthodes
        def __init__(self, driver):
            super().__init__(driver)

        def verifier_redirection_vers_page_cart(self):
           element =  self.verifier_le_texte_dun_champ(self.titre_cart_page)
           assert element == "Your Cart"

        def cliquer_sur_checkout(self):
            self.cliquer_sur_element(self.checkout_bouton)

        def verifier_que_le_panier_est_vide(self):
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.cart_quantity))