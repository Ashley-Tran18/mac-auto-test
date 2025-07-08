from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader


class AdminPage():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_timeout()

    def is_admin_menu_displayed(self):
        self.timeout =10
        admin = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Admin']"))
        )
        return  admin.is_enabled(), "Admin menu is not clickable" 
    

    def navigate_to_admin(self):
        admin = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Admin']"))
        )
        admin.click()


    def is_header_display(self):
        header = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, "//h6[contains(., 'Admin')]"))
        )
        return header.is_displayed(), "Admin/User Management page not visible"

