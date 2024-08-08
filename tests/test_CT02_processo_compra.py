import time
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.cartPage import CartPage
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TesteCT02:
    def test_ct02_adicionar_produtos_carrinho(self):
        #login
        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Onesie'

        login = LoginPage()
        login.fazer_login("standard_user","secret_sauce")

        #Add item
        home_page = HomePage()
        home_page.adicionar_ao_carrinho(produto_1)

        #Verificando item
        home_page.acessar_cartpage()
        time.sleep(5)
        cart_page = CartPage()
        cart_page.verificar_se_item_existe(produto_1)
        time.sleep(5)

        #Retornando ao shopping
        cart_page.retornar_a_homepage()

        #Add outro item.
        home_page.adicionar_ao_carrinho(produto_2)

        #Verificando itens
        home_page.acessar_cartpage()
        cart_page.verificar_se_item_existe(produto_2)
        time.sleep(5)
