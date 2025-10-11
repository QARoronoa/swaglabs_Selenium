from utilities.baseClass import baseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObjects.homePage import homePage


class cartPage(baseClass) :

    def __init__(self, driver):
        self.driver = driver

    #locators
    nom_article= (By.CSS_SELECTOR, ".inventory_item_name")
    btn_remove = (By.XPATH, "//button[@class='btn_secondary cart_button']")
    btn_continue_shopping = (By.XPATH, "(//a[@href='./inventory.html'])[2]")
    btn_checkout = (By.XPATH, "//a[@class='btn_action checkout_button']")


    #methodes
    def verifier_que_les_article_sont_dans_le_panier(self):
        nom_article = []
        articles = self.driver.find_elements(*cartPage.nom_article)
        for name in articles:
            nom_article.append(name.text)
        return nom_article

    def cliquer_sur_le_bouton_remove(self):
        wait = WebDriverWait(self.driver, 10)
        bouton_remove = wait.until(expected_conditions.visibility_of_element_located(cartPage.btn_remove))
        bouton_remove.click()

    def verifier_que_le_panier_soit_vide(self):
        wait = WebDriverWait(self.driver, 10)
        bouton_remove_invisible = wait.until(expected_conditions.invisibility_of_element_located(cartPage.btn_remove))
        return bouton_remove_invisible

    def cliquer_sur_continueShoppinf(self):
        self.driver.find_element(*cartPage.btn_continue_shopping).click()

    def cliquer_sur_le_bouton_checkout(self):
        self.driver.find_element(*cartPage.btn_checkout).click()
