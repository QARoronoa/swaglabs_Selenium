import time
import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.DetailArticlePage import DetailArticlePage

@allure.feature('Page d\'accueil')
def test_verifier_tri_prix_après_navigation(setup):
    login_page=LoginPage(setup)
    home_page=HomePage(setup)
    detailArticle_page = DetailArticlePage(setup)

    with allure.step('se connecter'):
        login_page.remplir_le_champ_user('standard_user')
        login_page.remplir_le_champ_pwd('secret_sauce')
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step('effectuer un tri Z to A'):
        home_page.effectuer_un_tri('za')
        home_page.verifier_le_tri_Z_to_A()

    with allure.step('navigation dans la fiche d un article'):
        home_page.cliquer_sur_image_sauce_labs_backpack()

    with allure.step('clique sur le bouton back'):
        detailArticle_page.cliquer_sur_bouton_back()
        time.sleep(2)

    with allure.step('effectuer un tri A to Z'):
        home_page.verifier_le_tri_a_to_z()


