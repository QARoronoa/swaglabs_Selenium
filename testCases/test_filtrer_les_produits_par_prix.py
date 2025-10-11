import time

import pytest
from utilities.baseClass import baseClass
from pageObjects.homePage import homePage
from pageObjects.loginPage import loginPage
from Data.data import loginPageData


class Test_filtrer_des_articles_par_produits(baseClass):

    def test_filtrer_produits_par_prix(self, standarUser):
        log = self.getLogger()
        login_page = loginPage(self.driver)
        home_page = homePage(self.driver)

        try:

            # verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est {titre}")

            #Se connecter
            user = login_page.entrer_nom_utilisateur(standarUser["username"])
            log.info(f"Le nom utilisateur {user} est entrer dans le champ")
            pwd = login_page.enter_entrer_mot_de_passe(standarUser["password"])
            log.info(f"Le mot de passe '{pwd}' est inserer dans le champ")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page d acceuil")

            #filtrer par price high to low
            home_page.selectionner_le_filtre_prix_decroisant()
            log.info("les articles sont triés par prix decroissant")

            #verifier le tri decroissant
            prix_articles = home_page.capturer_les_prix_decroissant()
            log.info(f"les prix sont {prix_articles}, ils sont triés par ordre decroissant")

            # filtrer par price low to high
            home_page.selectionner_le_filtre_prix_croissant()
            log.info("les articles sont triés par prix croissant")

            #verifier le tri croissant
            prix_articles = home_page.capturer_les_prix_croissant()
            log.info(f"les prix sont {prix_articles}, ils sont triés par ordre croissant")




            time.sleep(8)
        except Exception as e:
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standarUser(self, request):
        return request.param
