import time
import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.CartPage import CartPAge
from PagesObject.CheckoutInformationPage import CheckoutInformationPage

@allure.feature("Gestion du Panier")
def test_verification_panier_vide(setup, formulaire_info):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = CartPAge(setup)
    checkoutInformation_page = CheckoutInformationPage(setup)

    with allure.step("Se connecter"):
        login_page.remplir_le_champ_user("standard_user")
        login_page.remplir_le_champ_pwd("secret_sauce")
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("cliquer_sur_panier"):
        home_page.cliquer_sur_le_panier()

    with allure.step('Le panier est vide'):
        cart_page.verifier_que_le_panier_est_vide()
