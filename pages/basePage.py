import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrarElemento(self, locator):
        return self.driver.find_element(*(locator))
    
    def encontrarElementos(self, locator):
        return self.driver.find_elements(*(locator))
    
    def escrever(self, locator, texto):
        self.encontrarElemento(locator).send_keys(texto)

    def clicar(self, locator):
        self.encontrarElemento(locator).click()

    def verificar_se_elemento_eh_exibido(self, locator):
        return self.encontrarElemento(locator).is_displayed()        

    def verificar_texto_elemento(self, locator):
        return self.encontrarElemento(locator).text() 

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verificar_se_elemento_existe_assert(self, locator):
        assert self.encontrarElemento(locator), f'Elemento {locator} não existe, porém era esperado.'

    def verificar_se_elemento_nao_existe_assert(self, locator):
        assert len(self.encontrarElemento(locator)) == 0, f'Elemento {locator} existe, porém não era esperado.'

    def clicar_duas_vezes(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()
            
    def clicar_btn_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()
        
    def pressionar_tecla(self, locator, key):
        elemento = self.encontrarElemento(locator)
        if key == "ENTER":
            elemento.send_keys(Keys.ENTER)
        elif key == "ESPACO":
            elemento.send_keys(Keys.SPACE)
