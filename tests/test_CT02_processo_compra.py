import conftest
import time
from pages.loginPage import LoginPage
from pages.homePage import HomePage
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TesteCT02:
    def test_ct02_adicionar_produtos_carrinho(self):
        #login
        login = LoginPage()
        login.fazer_login("standard_user","secret_sauce")

        #Add item
        home_page = HomePage()

        home_page.adicionar_ao_carrinho('Sauce Labs Backpack')

        #Verificando item
        home_page.verificar_item_adicionado()
        time.sleep(5)

        #Retornando ao shopping
        home_page.retornar_a_homepage()

        #Add outro item.
        home_page.adicionar_ao_carrinho('Sauce Labs Onesie')

        #Verificando itens
        home_page.verificar_item_adicionado()
        time.sleep(5)