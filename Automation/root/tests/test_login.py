# tests/test_login.py

from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
import allure

class TestLogin(BaseTest):
    @allure.story("Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        login_page = LoginPage(self.driver) # sở hữu các chức năng có trong login page, bắt buộc phải truyền self.driver
        # cách 1
        # login_page.enter_username(ConfigReader.get_username())
        # login_page.enter_password(ConfigReader.get_password())
        # login_page.login_btn()               
        
        # cách 2
        # username, password = ConfigReader.get_username_password()
        # login_page.login(username, password)

        # cách 3
        login_page.login(*ConfigReader.get_username_password()) # Dấu * sẽ giải nén tuple "Admin", "admin123" thành 2 đối số riêng biệt.
        

        assert "dashboard" in self.driver.current_url.lower()







        
        


