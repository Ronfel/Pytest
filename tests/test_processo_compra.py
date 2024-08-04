from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.google.com")

browser.maximize_window()
browser.implicitly_wait(5)

browser.get("https://www.saucedemo.com/v1/")
#login
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
button = browser.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
button.click()

#Add item
browser.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']").click()
browser.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

#Verificando item
browser.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
time.sleep(5)

#Retornando ao shopping
browser.find_element(By.XPATH, "//*[@class='btn_secondary']").click()

#Add outro item.
browser.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Onesie']").click()
browser.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

#Verificando itens
browser.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
time.sleep(5)
