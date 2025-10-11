import time

import pytest
from utilities.baseClass import baseClass
from Data.data import loginPageData
from Data.data import datacheckoutInformation
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage
from pageObjects.cartPage import cartPage
from pageObjects.checkoutPage import checkoutPage

class Test_verifier_le_processus_HA(baseClass):

    def test_endToendHA(self, standardUser, checkout):
        login_page = loginPage(self.driver) # type: ignore
        home_page = homePage(self.driver) # type: ignore
        cart_page = cartPage(self.driver) # type: ignore
        checkout_page = checkoutPage(self.driver) # type: ignore
        log = self.getLogger()

        try :

            #verifier le titre de la page
            titre = self.verifier_le_titre ("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f" Le titre de la page est {titre}")

            #Se connecter
            user = login_page.entrer_nom_utilisateur(standardUser["username"])
            log.info(f"Le nom utilisateur {user} est entrer dans le champ")
            pwd = login_page.enter_entrer_mot_de_passe(standardUser["password"])
            log.info(f"Le mot de passe '{pwd}' est inserer dans le champ")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page d acceuil")

            # Ajouter des articles dans le panier
            home_page.cliquer_le_bouton_add_to_cart_1()
            home_page.cliquer_le_bouton_add_to_cart_2()
            log.info("Les articles sont ajoute dans le panier")

            # Verifier que le chiffre 2 s'affiche au niveau du panier
            chiffre_panier = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            log.info(f"le chiffre '{chiffre_panier}' s affiche près du panier")

            # verifier que les articles sont dans le panier
            home_page.cliquer_sur_le_panier()
            log.info("Redirection vers la page panier")
            nomArticles = cart_page.verifier_que_les_article_sont_dans_le_panier()
            log.info(f"Les articles '{nomArticles}' sont bien dans le panier !")

            #cliquer sur le boutton checkout
            cart_page.cliquer_sur_le_bouton_checkout()
            log.info("Redirection vers la page Checkout")

            #verifier que la redirection vers la page checkout
            titre = checkout_page.verifieer_le_titre_de_la_page_checkout()
            assert titre == "Checkout: Your Information"
            log.info(f"Le titre de la page est '{titre}' !")

            #remplir le formulaire checkout information
            firstName = checkout_page.sairsir_le_champ_firstname(checkout["firstname"])
            lastName = checkout_page.sairsir_le_champ_lastname(checkout["lastname"])
            codePostal = checkout_page.sairsir_le_champ_zipcode(checkout["zipCode"])
            log.info(f"le prenom '{firstName}', le nom '{lastName}' et le CP '{codePostal}' s'affichent dans les champs respectifs")
            checkout_page.cliquer_sur_continue()
            log.info("Redirection vers la page ")

            #finaliser la commande
            checkout_page.cliquer_sur_finish()
            log.info("redirection vers la page confirmation ")

            #verifier le message de confirmation
            mess = checkout_page.verifier_le_message_confirmant_la_commande()
            log.info(f"Le message '{mess}' confirme la commande")

            #se deconnecter
            home_page.cliquer_sur_le_bouton_burger()
            home_page.cliquer_sur_le_bouton_logout()
            log.info("redirection vers la page de connexion")

        except Exception as e:
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser(self, request):
        return request.param

    @pytest.fixture(params=datacheckoutInformation.test_data_checkout)
    def checkout(self, request):
        return request.param