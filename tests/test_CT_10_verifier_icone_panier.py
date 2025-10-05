import allure

from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage


@allure.feature("Gestion du Panier")
def test_verifier_icone_panier(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)


    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step('ajouter un article au panier'):
        home_page.cliquer_sur_add_to_cart_Sauce_Labs_Backpack()

    with allure.step('quantite badge panier = 1'):
        home_page.verifier_la_quantite_affiche_sur_badge_panier('1')

    with allure.step('quantite badge panier = 2'):
        home_page.cliquer_sur_add_to_cart_Sauce_Labs_Bolt_T_Shirt()
        home_page.verifier_la_quantite_affiche_sur_badge_panier('2')


