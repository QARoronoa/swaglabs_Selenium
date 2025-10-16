import time

import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.DetailArticlePage import DetailArticlePage



@allure.feature('Page d\'accueil')
def test_verifier_tri(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)

    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Tri de Z to A"):
        home_page.effectuer_un_tri("za")
        home_page.verifier_le_tri_Z_to_A()

    with allure.step("Tri de Z to A"):
        home_page.effectuer_un_tri("az")
        home_page.verifier_le_tri_a_to_z()

