import conftest
from pages.loginPage import LoginPage
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInval
class TesteCT03:
    
    def test_CT03_msg_texto_erro_login(self):
        textoErroEsperado = 'Epic sad: Username and password do not match any user in this service'

        driver = conftest.driver
        login_Page = LoginPage()
        login_Page.fazer_login("x","X")
        driver.implicitly_wait(5)

        assert login_Page.login_invalido()

        login_Page.verificar_texto_erro_login(textoErroEsperado)         

