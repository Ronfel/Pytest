import conftest
from pages.loginPage import LoginPage
import pytest
from pages.homePage import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginVal
class TesteCT01:
    @pytest.mark.loginVal
    def test_CT01_login_valido(self):
        login_Page = LoginPage()
        login_Page.fazer_login("standard_user","secret_sauce")

        home_page = HomePage()       
        assert home_page.verificar_login
         

