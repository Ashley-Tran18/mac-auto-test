from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.config_reader import ConfigReader

class TestAdmin(BaseTest):
    def test_admin_navigation(self):
        login_page = LoginPage(self.driver)
        login_page.login(*ConfigReader.get_username_password())

        admin_page = AdminPage(self.driver)  # truyền driver từ BaseTest
        admin_page.navigate_to_admin()  # gọi hàm để test admin navigation
        
        # check = admin_page.is_admin_menu_displayed() -> failed
        # assert check == True

        # cách 1
        # check, _ = admin_page.is_admin_menu_displayed()
        # assert check is True   

        # cách 2
        check, message = admin_page.is_admin_menu_displayed()
        assert check, message
 

