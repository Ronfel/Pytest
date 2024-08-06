from selenium.webdriver.common.by import By
import conftest
from pages.basePage import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.btn_retornar_a_home = (By.XPATH, "//*[@class='btn_secondary']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text() = '{}']")

    def verificar_se_item_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))  
        self.verificar_se_elemento_existe(item)      

    def retornar_a_homepage(self):
        self.clicar(self.btn_retornar_a_home)

         
