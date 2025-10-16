import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.DetailArticlePage import DetailArticlePage



@allure.feature('Page d\'accueil')
def test_verifier_redirection_vers_fiche_produit(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)
    detailArticle_page = DetailArticlePage(setup)

    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("cliquer sur un article Backpack"):
        home_page.cliquer_sur_sauce_labs_backpack()

    with allure.step("La fiche du produit est visible"):
        detailArticle_page.verifier_la_redirection_vers_la_fiche_produit("Sauce Labs Backpack")

    with allure.step("Redirection vers la page d'accueil"):
        detailArticle_page.cliquer_sur_bouton_back()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Redirection vers la fiche produit"):
        home_page.cliquer_sur_image_sauce_labs_backpack()
        detailArticle_page.verifier_la_redirection_vers_la_fiche_produit("Sauce Labs Backpack")
