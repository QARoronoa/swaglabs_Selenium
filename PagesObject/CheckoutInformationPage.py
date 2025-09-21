from selenium.webdriver.common.by import By

from PagesObject.BasePage import BasePage


class CheckoutInformationPage(BasePage):



    #locators
        titre_cart_checkout_information = (By.CSS_SELECTOR, ".subheader")
        checkout_bouton = (By.XPATH, "//a[text()='CHECKOUT']")
        champ_firstName = (By.ID, "first-name")
        champ_lastName = (By.ID, "last-name")
        champ_cp = (By.ID, "postal-code")
        bouton_continue = (By.CSS_SELECTOR, ".cart_button")
        article_nom = (By.CSS_SELECTOR, ".inventory_item_name")
        finish_bouton = (By.CSS_SELECTOR, ".cart_button")
        thank_you_order_text = (By.CSS_SELECTOR, ".complete-header")

    # méthodes
        def __init__(self, driver):
            super().__init__(driver)

        def verifier_redirection_vers_page_checkout_information(self):
           element =  self.verifier_le_texte_dun_champ(self.titre_cart_checkout_information)
           assert element == "Checkout: Your Information"

        def remplir_le_formulaire(self, firtsName, lastName, cp):
            self.remplir_un_champ(self.champ_firstName, firtsName)
            self.remplir_un_champ(self.champ_lastName, lastName)
            self.remplir_un_champ(self.champ_cp, cp)

        def cliquer_sur_bouton_continue(self):
            self.cliquer_sur_element(self.bouton_continue)

        def verifier_article_panier(self):
            item_text = self.verifier_le_texte_dun_champ(self.article_nom)
            assert item_text == "Sauce Labs Backpack"

        def cliquer_sur_finish(self):
            self.cliquer_sur_element(self.finish_bouton)

        def verifier_message_order_success(self):
            titre_success_order = self.verifier_le_texte_dun_champ(self.thank_you_order_text)
            assert "THANK YOU" in titre_success_order

