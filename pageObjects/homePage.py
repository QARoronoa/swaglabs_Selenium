from selenium.webdriver.common.by import By
from utilities.baseClass import baseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

class homePage(baseClass):

    def __init__(self, driver):
        self.driver = driver

    #locators
    btn_addToCart = (By.XPATH, "(//button[@class='btn_primary btn_inventory'])")
    btn_addToCart_1 = (By.XPATH, "(//button[@class='btn_primary btn_inventory'])[1]")
    btn_addToCart_2 = (By.XPATH, "(//button[@class='btn_primary btn_inventory'])[2]")
    chiffre_panier = (By.XPATH, "//span[@class='fa-layers-counter shopping_cart_badge']")
    logo_panier = (By.ID, "shopping_cart_container")
    btn_burger = (By.CSS_SELECTOR, ".bm-burger-button")
    btn_logout = (By.ID, "logout_sidebar_link")
    btn_filtre_product = (By.CSS_SELECTOR, ".product_sort_container")
    prix_articles = (By.CSS_SELECTOR, ".inventory_item_price")
    nom_articles = (By.CSS_SELECTOR, ".inventory_item_name")



    #methodes
    def cliquer_le_bouton_add_to_cart_1(self):
        self.driver.find_element(*homePage.btn_addToCart_1).click()

    def cliquer_le_bouton_add_to_cart_2(self):
        self.driver.find_element(*homePage.btn_addToCart_1).click()

    def verifier_la_presence_du_chiffre_sur_le_panier(self):
        wait = WebDriverWait(self.driver, 10)
        quantity_cart = wait.until(expected_conditions.visibility_of_element_located(homePage.chiffre_panier))
        return quantity_cart.text

    def cliquer_sur_le_panier(self):
        self.driver.find_element(*homePage.logo_panier).click()

    def cliquer_sur_le_bouton_burger(self):
        wait = WebDriverWait(self.driver, 10)
        btn_menu = wait.until(expected_conditions.visibility_of_element_located(homePage.btn_burger))
        btn_menu.click()

    def cliquer_sur_le_bouton_logout(self):
        wait = WebDriverWait(self.driver, 10)
        logout = wait.until(expected_conditions.presence_of_element_located(homePage.btn_logout))
        logout.click()

    def selectionner_le_filtre_prix_decroisant(self):
        dropdown_element = self.driver.find_element(*homePage.btn_filtre_product)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("hilo")

    def capturer_les_prix_decroissant(self):
        prix_element = self.driver.find_elements(*homePage.prix_articles)
        prix_trié_decroissant = []
        for prix in prix_element:
            prix_trié_decroissant.append(prix.text)
        return prix_trié_decroissant

    def selectionner_le_filtre_prix_croissant(self):
        dropdown_element = self.driver.find_element(*homePage.btn_filtre_product)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("lohi")

    def capturer_les_prix_croissant(self):
        prix_aricles = self.driver.find_elements(*homePage.prix_articles)
        prix_trié_croissant = []
        for prix in prix_aricles:
            prix_trié_croissant.append(prix.text)
        return prix_trié_croissant

    def selectionner_filtre_de_A_Z(self):
        dropdown_element = self.driver.find_element(*homePage.btn_filtre_product)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text("Name (A to Z)")

    def selectionner_filtre_de_Z_A(self):
        dropdown_element = self.driver.find_element(*homePage.btn_filtre_product)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("za")


    def capturer_le_nom_des_articles(self):
        nom_articles = self.driver.find_elements(*homePage.nom_articles)
        nom_articles_tries = []
        for nom in nom_articles:
            nom_articles_tries.append(nom.text)
        return nom_articles_tries
    
    def ajouter_tous_les_articles_dans_le_panier(self):
        btnAjouter_element = self.driver.find_elements(*homePage.btn_addToCart)
        for btn in btnAjouter_element:
            btn.click()









