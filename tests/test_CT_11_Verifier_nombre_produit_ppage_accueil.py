import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage



@allure.feature('Page d\'accueil')
def test_verifier_nombre_article_page_dacceuil(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)

    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Nombre d'article = 6"):
        home_page.verifier_nombre_de_produits()