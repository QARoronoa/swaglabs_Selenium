import allure
from PagesObject.LoginPage import LoginPage

@allure.feature("Authentification")
def test_connexion_echouee(setup):
    login_page = LoginPage(setup)

    with allure.step("Saisir standard_user dans Username."):
        login_page.remplir_le_champ_user("standard_user")

    with allure.step("Saisir un mot de passe incorrect."):
        login_page.remplir_le_champ_pwd("IEIEI")

    with allure.step("Cliquer sur le bouton Login"):
        login_page.cliquer_sur_login()

    with allure.step("Un message d’erreur s’affiche"):
        login_page.verifier_le_message_erreur_connexion()