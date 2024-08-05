from selenium.webdriver.common.by import By
import conftest
from pages.basePage import BasePage

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "*//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text() = '{}']")
        self.btn_add_ao_carrinho = (By.XPATH, "//*[text()='ADD TO CART']")   
        self.lista_itens_adicionados = (By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']")    
        self.btn_retornar_a_home = (By.XPATH, "//*[@class='btn_secondary']")


    def verificar_login(self, user, pword):
        return self.visivel(self.titulo_pagina)
    
    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.btn_add_ao_carrinho)

    def verificar_item_adicionado(self):
        self.clicar(self.lista_itens_adicionados)

    def retornar_a_homepage(self):
        self.clicar(self.btn_retornar_a_home)

         
