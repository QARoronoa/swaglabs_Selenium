import time

import pytest

from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage
from pageObjects.cartPage import cartPage
from Data.data import loginPageData


class Test_ajouter_un_article_au_panier(baseClass):

    def test_add_product_to_cart(self, standardUser):
        login_page = loginPage(self.driver)
        home_page = homePage(self.driver)
        cart_page = cartPage(self.driver)
        log = self.getLogger()

        try :

            #verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert "Swag Labs" == titre
            log.info(f"Le titre de la page est '{titre}'")

            #Se connecter avec standard user
            login_page.entrer_nom_utilisateur(standardUser["username"])
            login_page.enter_entrer_mot_de_passe(standardUser["password"])
            login_page.cliquer_sur_le_btn_login()
            log.info("Connexion reussie redirection vers la page d acceuil")

            #Ajouter un article dans le panier
            home_page.cliquer_le_bouton_add_to_cart_1()
            log.info("L article est ajouter dans le panier")

            #Verifier que le chiffre 1 s'affiche au niveau du panier
            chiffre_panier = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            log.info(f"Le chiffre afficher sur le panier est '{chiffre_panier}'")

            #ajouter un second article
            home_page.cliquer_le_bouton_add_to_cart_2()
            log.info("L article est ajouter dans le panier")

            # Verifier que le chiffre 2 s'affiche au niveau du panier
            chiffre_panier = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            log.info(f"le chiffre '{chiffre_panier}' s affiche près du panier")

            # Cliquer sur le panier
            home_page.cliquer_sur_le_panier()
            log.info("Redirection vers la page panier")

            # verifier que les articles sont dans le panier
            nomArticles = cart_page.verifier_que_les_article_sont_dans_le_panier()
            log.info(f"Les articles '{nomArticles}' sont bien dans le panier !")

            #supprimer un article du panier
            cart_page.cliquer_sur_le_bouton_remove()
            log.info("L article 'Sauce Labs Backpack' est supprimé du panier !")

            #revenir sur la page d'acceuil est verifié que le chiffre 1 s'affiche sur le panier
            cart_page.cliquer_sur_continueShoppinf()
            log.info("redirection vers la page d'acceuil")
            chiffre_panier = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            log.info(f"Le chiffre afficher sur le panier est '{chiffre_panier}'")
            assert chiffre_panier == "1"

            #se deconnecter
            home_page.cliquer_sur_le_bouton_burger()
            home_page.cliquer_sur_le_bouton_logout()
            log.info("redirection vers la page d'acceuil")

        
        except Exception as e:
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser(self, request):
        return request.param