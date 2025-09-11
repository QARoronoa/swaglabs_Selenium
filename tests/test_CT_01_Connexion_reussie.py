import time

import allure

from PagesObject.LoginPage import LoginPage
from PagesObject.HomePage import HomePage

@allure.feature("Authentification")
@allure.story("Connexion réussie avec utilisateur standard")

def test_connexion_reussie(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    with allure.step("Saisir standard_user dans le champ Username"):
        login_page.remplir_le_champ_user()

    with allure.step("saisir secret_sauce dans le champ Password"):
        login_page.remplir_le_champ_pwd()

    with allure.step("Cliquer sur le bouton Login"):
        login_page.cliquer_sur_login()

    with allure.step("L’utilisateur est redirigé vers la page des produits"):
        home_page.verifier_la_redirection_vers_homePage()

