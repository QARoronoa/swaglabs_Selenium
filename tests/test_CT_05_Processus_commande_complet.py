import time
import allure
from PagesObject.HomePage import HomePage
from PagesObject.LoginPage import LoginPage
from PagesObject.CartPage import CartPAge
from PagesObject.CheckoutInformationPage import CheckoutInformationPage

@allure.feature("Order")
def test_processus_commande_complet(setup, formulaire_info):
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

    with allure.step("Ouverture du panier"):
        home_page.cliquer_sur_le_panier()
        cart_page.verifier_redirection_vers_page_cart()

    with allure.step("Clique sur le bouton checkout"):
        cart_page.cliquer_sur_checkout()
        checkoutInformation_page.verifier_redirection_vers_page_checkout_information()

    with allure.step("remplir le formulaire"):
        checkoutInformation_page.remplir_le_formulaire(formulaire_info["firtsName"],
                                                       formulaire_info["lastName"],
                                                       formulaire_info["cp"])
        checkoutInformation_page.cliquer_sur_bouton_continue()
        checkoutInformation_page.verifier_article_panier()
        checkoutInformation_page.cliquer_sur_finish()

    with allure.step('Un message de confirmation apparaît : "THANK YOU FOR YOUR ORDER".'):
        checkoutInformation_page.verifier_message_order_success()
