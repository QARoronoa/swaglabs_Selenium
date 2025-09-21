from selenium.webdriver.common.by import By

from PagesObject.BasePage import BasePage


class CartPAge(BasePage):



    #locators
        titre_cart_page = (By.CSS_SELECTOR, ".subheader")
        checkout_bouton = (By.XPATH, "//a[text()='CHECKOUT']")



    # méthodes
        def __init__(self, driver):
            super().__init__(driver)

        def verifier_redirection_vers_page_cart(self):
           element =  self.verifier_le_texte_dun_champ(self.titre_cart_page)
           assert element == "Your Cart"

        def cliquer_sur_checkout(self):
            self.cliquer_sur_element(self.checkout_bouton)