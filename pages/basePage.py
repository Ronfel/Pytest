import conftest


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

    def verificar_se_elemento_existe(self, locator):
        return self.encontrarElemento(locator).is_displayed()        

    def verificar_texto_elemento(self, locator):
        return self.encontrarElemento(locator).text    
        
        
