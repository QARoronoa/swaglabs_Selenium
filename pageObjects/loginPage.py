from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.baseClass import baseClass


class loginPage(baseClass):

    def __init__(self, driver):
        self.driver = driver


    #locators
    userName = (By.ID, "user-name")
    passWord = (By.ID, "password")
    btn_login = (By.ID, "login-button")
    mess_erreur_login = (By.XPATH, "//h3[@data-test='error']")
    logo_robot = (By.CSS_SELECTOR, ".bot_column")

    #methodes
    def entrer_nom_utilisateur(self,user):
        pseudo = self.driver.find_element(*loginPage.userName)
        pseudo.send_keys(user)
        return pseudo.get_attribute('value')

    def enter_entrer_mot_de_passe(self, pwd):
        mdp = self.driver.find_element(*loginPage.passWord)
        mdp.send_keys(pwd)
        return mdp.get_attribute('value')

    def cliquer_sur_le_btn_login(self):
        self.driver.find_element(*loginPage.btn_login).click()

    def verifier_la_presence_du_message_erreur(self):
        mess_erreur= self.driver.find_element(*loginPage.mess_erreur_login)
        return mess_erreur.text

    def verifier_la_presence_du_logo_robot(self):
        wait = WebDriverWait(self.driver, 30)
        logo = wait.until(expected_conditions.visibility_of_element_located(loginPage.logo_robot))






