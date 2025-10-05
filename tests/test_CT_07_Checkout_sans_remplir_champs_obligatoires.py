import time
import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.CartPage import CartPAge
from PagesObject.CheckoutInformationPage import CheckoutInformationPage

@allure.feature("Order")
def test_checkout_sans_remplir_champs_obligatoires(setup, formulaire_info):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = CartPAge(setup)
    checkoutInformation_page = CheckoutInformationPage(setup)

    with allure.step("Se connecter"):
        login_page.remplir_le_champ_user("standard_user")
        login_page.remplir_le_champ_pwd("secret_sauce")
        login_page.cliquer_sur_login()
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Ajouter un article dans le panier"):
        home_page.cliquer_sur_add_to_cart_Sauce_Labs_Backpack()
        home_page.cliquer_sur_le_panier()
        cart_page.verifier_redirection_vers_page_cart()

    with allure.step("Clique sur le bouton checkout"):
        cart_page.cliquer_sur_checkout()
        checkoutInformation_page.verifier_redirection_vers_page_checkout_information()
        checkoutInformation_page.cliquer_sur_bouton_continue()

    with allure.step('Le message d erreur est visible : "Error"'):
        checkoutInformation_page.verifier_la_presence_du_message_derreur()


    time.sleep(5)