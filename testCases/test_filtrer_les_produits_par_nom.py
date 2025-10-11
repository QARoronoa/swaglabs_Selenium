import time

import pytest

from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage
from Data.data import loginPageData

class Test_filtrer_les_produits_par_nom(baseClass):

    def test_filtrer_produits_par_nom(self, standardUser):
        login_page = loginPage(self.driver)
        home_page = homePage(self.driver)
        log = self.getLogger()


        try:

            #verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est '{titre}'")

            #se connecter
            user = login_page.entrer_nom_utilisateur(standardUser["username"])
            log.info(f"Le nom  utilisateur '{user}' s'affiche dans le champ")
            pwd = login_page.enter_entrer_mot_de_passe(standardUser["password"])
            log.info(f"Le mdp '{pwd}' est entré dans le champ !")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page d'acceuil")

            #filtrer par ordre alphabétique de A à Z
            home_page.selectionner_filtre_de_A_Z()
            log.info("Les artilcles sont trier par ordre alphabétique de A à Z")

            #verifier le tri alphabétique de A à Z
            articles_triés = home_page.capturer_le_nom_des_articles()
            log.info(f"Les articles '{articles_triés}' sont triés")

            #filtrer par ordre alphabétique de Z à A
            home_page.selectionner_filtre_de_Z_A()
            log.info("Les artilcles sont trier par ordre alphabétique de Z à A")

            # verifier le tri alphabétique de Z à A
            articles_triés = home_page.capturer_le_nom_des_articles()
            log.info(f"Les articles '{articles_triés}' sont triés")


        except Exception as e:
            log.error(f"L erreur est dû au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser(self, request):
        return request.param