import time
import pytest
from Data.data import loginPageData
from utilities.baseClass import baseClass
from pageObjects.loginPage import loginPage
from pageObjects.homePage import homePage


class Test_seDeconnecter(baseClass):

    def test_logout(self, standardUser):
        log = self.getLogger()
        home_page = homePage(self.driver)
        login_page = loginPage(self.driver)


        try :

            #verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est '{titre}'")

            #se connecter
            username = login_page.entrer_nom_utilisateur(standardUser["username"])
            log.info(f"'{username}' s affiche dans le champ")
            password = login_page.enter_entrer_mot_de_passe(standardUser["password"])
            log.info(f"Le mot de passe {password} est entré dans le champ")
            login_page.cliquer_sur_le_btn_login()
            log.info("redirection vers la page dacceuil")

            #cliquer sur le bouton burger
            home_page.cliquer_sur_le_bouton_burger()
            log.info("Le menu souvre a gauche de l ecran")

            #cliquer sur le boutton logout
            home_page.cliquer_sur_le_bouton_logout()
            log.info("Redirection vers la page de connexion")

            #verifier la presence du logo
            login_page.verifier_la_presence_du_logo_robot()
            log.info("Le logo est visible")

        except Exception as e:
            log.error(f"L erreur est dû au{str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_standard_user)
    def standardUser(self, request):
        return request.param