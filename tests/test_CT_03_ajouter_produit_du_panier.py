import time
import allure
from PagesObject.LoginPage import LoginPage
from PagesObject.HomePage import HomePage

@allure.feature("Gestion du Panier")

def test_ajout_panier(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    with allure.step("Saisir standard_user dans le champ Username"):
        login_page.remplir_le_champ_user("standard_user")

    with allure.step("saisir secret_sauce dans le champ Password"):
        login_page.remplir_le_champ_pwd("secret_sauce")

    with allure.step("Cliquer sur le bouton Login"):
        login_page.cliquer_sur_login()

    with allure.step("L’utilisateur est redirigé vers la page des produits"):
        home_page.verifier_la_redirection_vers_homePage()

    with allure.step("Cliquer sur Add to cart pour le produit Sauce Labs Backpack"):
        home_page.cliquer_sur_add_to_cart_Sauce_Labs_Backpack()

    with allure.step("l'article est ajouté au panier"):
        home_page.verifier_la_quantite_affiche_sur_badge_panier("1")


