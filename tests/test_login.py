from selenium.webdriver.common.by import By
import conftest
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class LoginPage:

    def __init__(self):
        self.driver = conftest.driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginbutton = (By.ID,"login-button")


    def fazer_login(self, user, pword):
        #login 
        
        username = self.driver.find_element(*(self.username))
        password = self.driver.find_element(*(self.password))
        button   = self.driver.find_element(*(self.loginbutton))

        username.send_keys(user)
        password.send_keys(pword)
        button.click()

