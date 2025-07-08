from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep

class VacanciesPage():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_timeout()

    # navigate to recruitment page
    def navigate_to_recruitment(self):
        recruitment = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Recruitment']"))
        )
        recruitment.click()
    
    # navigate to vacancies tab
    def navigate_to_vacancies(self):
        vacancies_tab = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//a[text() = 'Vacancies']")
        )
        vacancies_tab.click()
    
    # Click Add button -> Add Vacancy
    def click_add_button(self):
        add_btn = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//button[contains(@class, 'button--secondary') and @type= 'button']")
        ) 
        add_btn.click()
    
    #  get data from json file
    def add_vacancy(self, vacancy_data):
        vacancy_name = vacancy_data['vacancy_name']
        job_title = vacancy_data['job_title']
        description = vacancy_data['description']
        number_of_position = vacancy_data['number_of_position']

        # fill in vacancy name
        vacancy_name_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//label[text()='Vacancy Name']/ancestor::div[contains(@class, 'oxd-input-group')]/descendant::input")
        )
        vacancy_name_input.send_keys(vacancy_name)
        
        # click on dropdown to select Job Title
        job_title_dropdown = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//div[@class = 'oxd-select-text-input']")
        )
        job_title_dropdown.click()

        # select Job Title option in dropdown
        select_job_title = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, f"//div[@role='listbox']//span[text()='{job_title}']")
        )
        select_job_title.click()
        
        # fill in the description 
        description_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//textarea[@placeholder='Type description here']")
        )
        description_input.send_keys(description)
        
        # find Admin name element
        admin_element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class = 'oxd-userdropdown-tab']"))
        )
        admin_name = admin_element.text.strip()
        print(f"Admin name extracted: '{admin_name}'")
        
        # input the name in Hiring Manager field
        hiring_manager_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//label[text()='Hiring Manager']//following::input[@placeholder='Type for hints...']")
        )
        # fill in the name on the hiring_manager_input field
        hiring_manager_input.send_keys(admin_name)
        sleep(2)
        # Use ActionChains to move to the first suggestion and click it
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        sleep(5)

        # fill in number
        number_of_position_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//label[text()='Number of Positions']//following::input[@class='oxd-input oxd-input--active']")
        )
        number_of_position_input.send_keys(number_of_position)


        # find the hidden Active checkbox input element
        active_checkbox = WebDriverWait(self.driver, self.timeout).until(
             lambda d: d.find_element(By.XPATH, "//p[text()='Active']/ancestor::div[contains(@class,'orangerhrm-switch-wrapper')]/descendant::input[@type='checkbox']")
        )
        # check if checkbox is ON
        is_on = active_checkbox.is_selected()
        print("Active is on?", is_on)
        # turn OFF if is ON
        if is_on:
            self.driver.execute_script("arguments[0].click();",active_checkbox)

        # find the hidden Publish checkbox input element
        publish_toggle = WebDriverWait(self.driver, self.timeout).until(
             lambda d: d.find_element(By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']/ancestor::div[contains(@class,'orangerhrm-switch-wrapper')]/descendant::input[@type='checkbox']")
        )
        # check if checkbox is ON
        is_on = publish_toggle.is_selected()
        # Turn ON if toggle OFF
        if is_on:
            print("Publish toggle is ON")
        else:
            self.driver.execute_script("arguments[0].click();", publish_toggle)
        
        # click on Save button 
        save_btn = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//button[@type ='submit']")
        )
        save_btn.click()
        sleep(5)
    

    # check if the vacancy is added successfully
    # def is_vacancy_added_successfully(self):
    #     toast = WebDriverWait(self.driver, self.timeout).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[@id='oxd-toaster_1']//p[text()= 'Successfully Saved']"))
    #     )
    #     return toast.text.strip()

        self.driver.back()
        sleep(10)

    def navigate_to_edit_vacancy(self):
        edit_btn = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//div[text()= 'Trần Ngọc Ngân Thảo']//following::i[@class= 'oxd-icon bi-pencil-fill']")
        )
        edit_btn.click()
    
    def is_edit_header_display(self):
        edit_header = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Edit Vacancy']"))
        )
        return edit_header.is_displayed(), "Edit page not visible"
    
    def cancel_edit(self):
        cancel_btn = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--ghost']")
        )
        cancel_btn.click()

    def is_vacancy_page_display(self):
        vacancy_header = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//a[text() = 'Vacancies']")
        )
        return vacancy_header.is_displayed(), "Vacancy page not visible"
    
    # 10.	Select Job Title = Automation Tester and Hiring Manager = current login user then click on Search button
    # 11.	Verify there is at least one items exist

    def filter_vacancy(self):
        select_job_title = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(By.XPATH, "//div[@role='listbox']//span[text()='Automaton Tester']")
        )
        select_job_title.select_by_visible_text("Automaton Tester")

        # select_hiring_manager = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(By.XPATH, "//span[@class = 'oxd-userdropdown-tab']")
        # )
        # select_hiring_manager.select_by_visible_text("")




    



  

         







    




    



        


        




