from selenium.webdriver.common.by import By
import conftest
from pages.basePage import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginbutton = (By.ID,"login-button")
        self.errologin = (By.XPATH, "//*[@data-test='error']")


    def fazer_login(self, user, pword):
        #login 
        self.escrever(self.username, user)
        self.escrever(self.password, pword)
        self.clicar(self.loginbutton)

    def login_invalido(self):
        return self.verificar_se_elemento_existe(self.errologin)
    
    def verificar_texto_erro_login(self, textoEsperado):
        textoEncontrado = self.verificar_texto_elemento(self.errologin)
        assert textoEncontrado == textoEsperado, f'O texto retornado foi: "{textoEncontrado}", mas o texto esperado é: "{textoEsperado}".'
