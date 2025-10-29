import time
import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.DetailArticlePage import DetailArticlePage

@allure.feature('Page d\'accueil')
def test_ajouter_les_6_articles_aux_panier(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)

    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step('clique sur les boutons "add to cart"'):
        home_page.cliquer_sur_les_boutons_add_to_cart()

    with allure.step('Le badge affiche 6'):
        home_page.verifier_la_quantite_affiche_sur_badge_panier("6")

    with allure.step('Les 6 bouton removes sont visibles'):
        home_page.verifier_les_boutons_remove_sont_visibles()
