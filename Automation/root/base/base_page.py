# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.config_reader import ConfigReader

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.timeout = ConfigReader.get_timeout()
        
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_reader import ConfigReader
class BasePage:
    def __init__(self, driver):
        self.driver = driver    
        self.timeout = 10
     
    def find_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*locator)
        )
        return element
    
    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text
 