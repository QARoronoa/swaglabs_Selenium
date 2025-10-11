import time

import pytest

from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from Data.data import loginPageData


class Test_connexionSauceDemo(baseClass):

    def test_connexion(self, standard_user):
        log = self.getLogger()
        login_page = loginPage(self.driver)


        try :
            #verifier le titre
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est {titre}")

            #Entrer l username
            Username = login_page.entrer_nom_utilisateur(standard_user["username"])
            log.info(f"{Username} est bien mis dans le champ")

            #Entrer le password
            password= login_page.enter_entrer_mot_de_passe(standard_user["password"])
            log.info(f"{password} est bien mis dans le champ")

            #Cliquer sur le bouton Login
            login_page.cliquer_sur_le_btn_login()
            log.info("Redirection vers la page d acceuil du site")

            #Verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est {titre}")

        except Exception as e:
            log.error(f"Erreur est du à str(e)")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standard_user(self, request):
        return request.param