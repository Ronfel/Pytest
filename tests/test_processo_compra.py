from selenium.webdriver.common.by import By
import conftest
import time
from pages.loginPage import LoginPage
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TesteCT02:
    def test_ct02_adicionar_produtos_carrinho(self):
        #login
        driver = conftest.driver

        login = LoginPage()

        login.fazer_login("standard_user","secret_sauce")

        #Add item
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        #Verificando item
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
        time.sleep(5)

        #Retornando ao shopping
        driver.find_element(By.XPATH, "//*[@class='btn_secondary']").click()

        #Add outro item.
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Onesie']").click()
        driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        #Verificando itens
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
        time.sleep(5)