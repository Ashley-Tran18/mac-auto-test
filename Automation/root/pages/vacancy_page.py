from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_reader import ConfigReader
from selenium.webdriver.support.ui import Select
from time import sleep
from base.base_page import BasePage

class VacancyPage(BasePage):
    def __init__(self, driver):
        self.timeout = 30
        self.driver = driver
        self.user_data = ConfigReader.get_vacancy_info()
        #xpath
        self.recruitment_menu = (By.XPATH, "//span[text()='Recruitment']")
        self.vacancy_tag = (By.XPATH, "//a[text()='Vacancies']")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.enter_name = (By.XPATH, "//label[text()='Vacancy Name']/following::input[@class='oxd-input oxd-input--active'][1]")
        self.choose_job = (By.XPATH, "//div[@class='oxd-select-text-input']")
        self.choose_job_dropdown = (By.XPATH, "//div[@role='listbox' and @loading='false']")
        self.enter_des = (By.XPATH, "//textarea[@placeholder='Type description here']")
        self.admin_name = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.enter_admin_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.hirring_dropdown = (By.XPATH, "//div[@role='listbox' and @loading='false']")
        self.numb_position = (By.XPATH, "//label[text()='Number of Positions']/following::input[@class='oxd-input oxd-input--active']")
        self.active_btn = (By.XPATH, "//p[contains(., 'Active')]/following::span[contains(@class, 'active')][1]")
        self.text_publish = (By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']")
        self.status_btn = (By.XPATH, "//p[contains(., 'Publish in RSS')]/following::span[contains(@class, 'active')]")
        self.save_btn = (By.XPATH, "//button[text()=' Save ']")
        self.edit_text = (By.XPATH, "//h6[text()='Edit Vacancy']")
        self.cancel_btn = (By.XPATH, "//button[text()=' Cancel ']")
        self.vacancy_text = (By.XPATH, "//h5[text()='Vacancies']")
        self.seach_btn = (By.XPATH, "//button[text()=' Search ']")
        self.search_hirring_manager = (By.XPATH, "//label[contains(text(), 'Hiring Manager')]/following::div[contains(text(), '-- Select --')]")
        self.search_result_text = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-row oxd-table-row--with-border']")
 
 
    def click_recruitment_menu(self):
        recruitment_nenu = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.recruitment_menu)
        )
        recruitment_nenu.click()
   
    def click_vacancy_tag(self):
        # vacancy_tag = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.vacancy_tag)
        # )
        vacancy_tag= self.find_element(self.vacancy_tag)
        vacancy_tag.click()
 
    def click_add_btn(self):
        self.driver.find_element(*self.add_btn).click()
   
    def enter_vacancy_name(self):
        vacancy_name = self.user_data["vacancy_name"]
        # enter_name = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.enter_name)
        # )
        self.send_keys(self.enter_name, vacancy_name)
 
    def choose_job_title(self):
        job_title = self.user_data["job_title"]
        # job_dropdown = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.choose_job)
        # )
        # job_dropdown.click()
        self.click(self.choose_job)
 
        WebDriverWait(self.driver, self.timeout).until(
            EC. presence_of_all_elements_located(self.choose_job_dropdown)
        )
        # selected = self.driver.find_element(*self.choose_job).text
        # selected.click()
        dropdown_element = self.driver.switch_to.active_element
        for _ in range(10):  # thử tối đa 10 lần
            dropdown_element.send_keys(Keys.ARROW_DOWN)
            sleep(2)  # đợi UI cập nhật
            selected = self.driver.find_element(*self.choose_job).text
            if selected.strip() == job_title:
                dropdown_element.send_keys(Keys.ENTER)
                return
        raise Exception("❌ Không tìm thấy lựa chọn 'Admin' trong dropdown")
   
    def enter_description(self):
        description = self.user_data["description"]
        # enter_description = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.enter_des)
        # )
        # enter_description.send_keys(description)
        self.send_keys(self.enter_des, description)
   
    def get_admin_name(self):
        get_name = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.admin_name)
        )
        admin_name = get_name.text
        print("tên account là", admin_name)
        hirring_manager = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.enter_admin_name)
        )
        hirring_manager.click()
        hirring_manager.send_keys(admin_name)
        sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(hirring_manager)
        actions.click()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform() #actions.perform là dòng code thực thi các code phía trên
    def enter_position(self):
        numb = self.user_data["number_of_position"]
        # enter_numb = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.numb_position)
        # )
        # enter_numb.send_keys(numb)
        self.send_keys(self.numb_position, numb)
    def is_active(self):
        toggle_active = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.active_btn)  
        )
 
        toggle_check = toggle_active.get_attribute("class")
       
        if "active" in toggle_check:  
            print("Toggle đang BẬT")
        else:
            toggle_active.click()
            print("Đã BẬT toggle")
 
    def switch_status_publish(self):
        toggle = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.status_btn)  
        )
 
        toggle_class = toggle.get_attribute("class")
       
        if "active" in toggle_class:  
            toggle.click()
            print("Đã tắt toggle.")
        else:
            print("Toggle đã ở trạng thái TẮT.")
 
       
        new_class = toggle.get_attribute("class")
        assert "active" not in new_class, "Toggle vẫn đang BẬT!"
   
    def click_save_btn(self):
        # save_btn = self.driver.find_element(*self.save_btn).click()
        self.click(self.save_btn)
        sleep(10)
    def check_edit_displayed(self):
        edit_displayed = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.edit_text)
        )
        return edit_displayed.text
    
    
    def click_cancel_btn(self):
        # cancel_btn = self.driver.find_element(*self.cancel_btn).click()
        self.click(self.cancel_btn)  
 
    def verify_vacancy_again(self):
        # vacancies_displayed = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d: d.find_element(*self.vacancy_text)
        # )
        # return vacancies_displayed.text
        return self.get_text(self.vacancy_text)
    def search_manager_name(self):
        get_name_admin = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.admin_name)
        )
        admin_name = get_name_admin.text
        print("tên account là", admin_name)
        search_hirring_manager = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.search_hirring_manager)
        )
        search_hirring_manager.click()
        search_hirring_manager.send_keys(admin_name)
        sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_hirring_manager)
        actions.click()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
 
    def search_employee(self):
        self.choose_job_title()
        self.search_manager_name()
 
        # search_btn = WebDriverWait(self.driver, self.timeout).until(
        #     EC.element_to_be_clickable(self.seach_btn)
        # )
        self.click(self.seach_btn)
    def verify_search_result(self):
        results = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_elements(*self.search_result_text)
        )
        count = len(results)
        print(f"Số kết quả tìm kiếm: {count}")
        if count > 1:
            print("Search Success")
        else:
            print("Search failed")