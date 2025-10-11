import time

import pytest
from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage
from pageObjects.cartPage import cartPage
from Data.data import loginPageData


class Test_suppression_article(baseClass):

    def test_delete_item_from_cart(self, standardUser):
        log = self.getLogger()
        home_page = homePage(self.driver)
        login_page = loginPage(self.driver)
        cart_page = cartPage(self.driver)

        try:

            #verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est '{titre}'")

            #se connecter
            user = login_page.entrer_nom_utilisateur(standardUser["username"])
            log.info(f"L username est '{user}'")
            pwd = login_page.enter_entrer_mot_de_passe(standardUser["password"])
            log.info(f"Le password est '{pwd}'")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page d acceuil")

            #ajouter un article au panier
            home_page.cliquer_le_bouton_add_to_cart_1()
            log.info("L article est ajouter dans le panier")
            chiffre_panier = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            log.info(f"Le chiffre afficher sur le panier est '{chiffre_panier}'")

            #cliquer sur le panier
            home_page.cliquer_sur_le_panier()
            log.info("Redirection vers la page panier")
            time.sleep(2)

            #supprimer l article du panier
            cart_page.cliquer_sur_le_bouton_remove()
            log.info("L article est supprimé du panier")

            #verifier que le panier n'affiche plus de chiffre
            btn = cart_page.verifier_que_le_panier_soit_vide()
            log.info(f"le boutonn'est plus visible : {btn} ")

        except Exception as e :
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser (self, request):
        return request.param