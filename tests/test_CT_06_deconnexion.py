import time

import allure

from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage

@allure.feature("Authentification")
def test_deconnexion(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    with allure.step("Se connecter"):
        login_page.remplir_le_champ_user("standard_user")
        login_page.remplir_le_champ_pwd("secret_sauce")
        login_page.cliquer_sur_login()

    with allure.step("Redirection vers la page d\'accueil"):
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Cliquer sur le bouton burger"):
        home_page.cliquer_sur_le_bouton_burger()

    with allure.step("Cliquer sur le bouton logout"):
        home_page.cliquer_sur_le_bouton_logout()

    with allure.step("Redirection vers la pge de connexion"):
        login_page.verifier_la_presence_du_bouton_login()

