import time

import pytest
from pageObjects.loginPage import loginPage
from Data.data import loginPageData
from utilities.baseClass import baseClass
from pageObjects.cartPage import cartPage


class Test_connexionEchoue(baseClass):

    def test_connexion_fail(self, incorrect_user):
        log = self.getLogger()
        login_page = loginPage(self.driver)
        cart_page = cartPage(self.driver)

        try:

            #Verifier le titre de la page
            titre = self.verifier_le_titre("Swag Labs")
            assert titre == "Swag Labs"
            log.info(f"Le titre de la page est {titre}")

            #Entrer l'username
            user = login_page.entrer_nom_utilisateur(incorrect_user["username"])
            log.info(f"L identifiant incorrect {user} s'affiche dans le champ")

            #Entrer le password
            pwd = login_page.enter_entrer_mot_de_passe(incorrect_user["password"])
            log.info(f"Le password incorrect {pwd} s'affiche dans le champ")

            #cliquer sur login
            login_page.cliquer_sur_le_btn_login()
            log.info("Un message d erreur saffiche")

            #verifier la presence du message d'erreur
            message_alerte = login_page.verifier_la_presence_du_message_erreur()
            log.info(f"Le message d alerte '{message_alerte}' s affiche bien")


        except Exception as e:
            log.error(f"l erreur est du au {str(e)}")
            raise

    @pytest.fixture(params=loginPageData.test_data_incorrect_user)
    def incorrect_user(self, request):
        return request.param



