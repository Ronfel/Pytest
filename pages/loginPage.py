from selenium.webdriver.common.by import By
import conftest
from pages.basePage import BasePage
import pytest

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginbutton = (By.ID,"login-button")


    def fazer_login(self, user, pword):
        #login 
        self.escrever(self.username, user)
        self.escrever(self.password, pword)
        self.clicar(self.loginbutton)
