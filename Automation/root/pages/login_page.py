# #  pages/login_page.py

#  Cách 1 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
        
#     def enter_username(self, username):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
#         ).send_keys(username)

#     def enter_password(self, password):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
#         ).send_keys(password)
    
#     def click_login(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']"))
#         ).click()


# Cách 2
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

# class LoginPage():
#     # khởi tạo page, truyền vào driver "__init__"
#     def __init__(self, driver):
#         self.timeout = 10
#         self.driver = driver
        
#         self.username_input = (By.XPATH, "//input[@name='username']")
#         self.password_input = (By.XPATH, "//input[@name='password']")
#         self.login_btn = (By.XPATH, "//button")

#     def enter_username(self, username: str):
#         username_input = WebDriverWait(self.driver, self.timeout).until(
#             lambda d: d.find_elements(*self.username_input)
#         )
#         username_input[0].send_keys(username)

#     def enter_password(self, password: str):
#         password_input = WebDriverWait(self.driver, self.timeout).until(
#             lambda d: d.find_elements(*self.password_input)
#         )
#         password_input[0].send_keys(password)

#     def click_login(self):
#         self.driver.find_elements(*self.login_btn)[0].click()

# Cách 3  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver

        self.username_input = (By.XPATH, "//input[@name = 'username']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_btn = (By.XPATH, "//button")

    def login(self, username, password):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((self.username_input))
        ).send_keys(username)
        
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
