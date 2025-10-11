import time
import pytest
from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage
from pageObjects.checkoutPage import checkoutPage
from pageObjects.cartPage import cartPage
from Data.data import loginPageData
from Data.data import datacheckoutInformation

class Test_comparerer_prix_total_et_prix_articles_panier(baseClass):

    def test_verif_prix_total(self, standardUser, checkoutInformation):

        login_page = loginPage(self.driver) # type: ignore
        home_page = homePage(self.driver) # type: ignore
        cart_page = cartPage(self.driver) # type: ignore
        checkout_page = checkoutPage(self.driver) # type: ignore
        log = self.getLogger()

        try:
            #verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert "Swag Labs" == titre
            log.info(f"Le titre de la page est {titre}")

            #Se connecter
            user = login_page.entrer_nom_utilisateur(standardUser["username"])
            log.info(f"Le nom utilisateur {user} est entrer dans le champ")
            pwd = login_page.enter_entrer_mot_de_passe(standardUser["password"])
            log.info(f"Le mot de passe '{pwd}' est inserer dans le champ")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page d acceuil")

            #ajouter tous les articles dans le panier
            home_page.ajouter_tous_les_articles_dans_le_panier()
            log.info("Tous les articles ont été ajouté dans le panier")

            #verifier que le panier affiche un chiffre 6
            chiffre = home_page.verifier_la_presence_du_chiffre_sur_le_panier()
            assert chiffre == "6"
            log.info(f"Le chiffre affiché est {chiffre}")

            #ouvrir le panier 
            home_page.cliquer_sur_le_panier()
            log.info(f"redirection vers la page cart")

            #cliquer sur checkout
            cart_page.cliquer_sur_le_bouton_checkout()
            log.info("redirection vers la page d'information")

            #remplir le formulaire et cliquer sur le bouton continue
            prenom = checkout_page.sairsir_le_champ_firstname(checkoutInformation["firstname"])
            log.info(f"Le prenom '{prenom}' s'affiche dans le champ firstname")

            nom = checkout_page.sairsir_le_champ_lastname(checkoutInformation["lastname"])
            log.info(f"Le nom'{nom}' s'affiche dans le champ lastname")

            zipCode = checkout_page.sairsir_le_champ_zipcode(checkoutInformation["zipCode"])
            log.info(f"Le zipCode '{zipCode}' s'affiche dans le champ zipCode")

            checkout_page.cliquer_sur_continue()
            log.info(f"redirection vers la page 'checkout overview'")

            #verifier que le total des prix artilces correspond au total
            prix_articles_total = checkout_page.verifier_que_la_somme_des_articles_correspond_au_total()
            assert prix_articles_total == 129.94
            log.info(f"le prix total s'élève à '{prix_articles_total}'")

            #cliquer sur finish et se deconnecter
            checkout_page.cliquer_sur_finish()
            home_page.cliquer_sur_le_bouton_burger()
            home_page.cliquer_sur_le_bouton_logout()
            log.info("redirection vers la page de connexion")

        except Exception as e:
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser (self, request) :
        return request.param
    
    @pytest.fixture(params=datacheckoutInformation.test_data_checkout)
    def checkoutInformation(self, request) :
        return request.param


        
