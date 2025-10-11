from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.baseClass import baseClass

class checkoutPage(baseClass):

    def __init__(self, driver):
        self.driver = driver


    #locators
    checkout_titre = (By.CSS_SELECTOR, ".subheader")
    firstName_ID = (By.ID, "first-name")
    lastName_ID = (By.ID, "last-name")
    zipCode_ID = (By.ID, "postal-code")
    btn_continue_XPATH = (By.XPATH, "//input[@value='CONTINUE']")
    btn_finish = (By.XPATH, "//a[@class='btn_action cart_button']")
    succes_message_CSS = (By.CSS_SELECTOR, ".complete-header")
    prix_articles = (By.CSS_SELECTOR, ".inventory_item_price")

    #methodes
    def verifieer_le_titre_de_la_page_checkout(self):
        titre = self.driver.find_element(*checkoutPage.checkout_titre)
        return titre.text

    def sairsir_le_champ_firstname(self, f_name):
        firstname = self.driver.find_element(*checkoutPage.firstName_ID)
        firstname.send_keys(f_name)
        return firstname.get_attribute("value")

    def sairsir_le_champ_lastname(self, l_name):
        lastname = self.driver.find_element(*checkoutPage.lastName_ID)
        lastname.send_keys(l_name)
        return lastname.get_attribute("value")

    def sairsir_le_champ_zipcode(self, cp):
        codePostal = self.driver.find_element(*checkoutPage.zipCode_ID)
        codePostal.send_keys(cp)
        return codePostal.get_attribute("value")

    def cliquer_sur_continue(self):
        self.driver.find_element(*checkoutPage.btn_continue_XPATH).click()

    def cliquer_sur_finish(self):
        self.driver.find_element(*checkoutPage.btn_finish).click()

    def verifier_le_message_confirmant_la_commande(self):
        mess = self.driver.find_element(*checkoutPage.succes_message_CSS)
        return mess.text
    
    def verifier_que_la_somme_des_articles_correspond_au_total(self):
        wait = WebDriverWait(self.driver, 10)
        total_price = wait.until(expected_conditions.presence_of_all_elements_located(checkoutPage.prix_articles))
        sum = 0
        for prix in total_price:
            sum = sum + float(prix.text.replace('$', '').strip())
        return sum
        
    
        





