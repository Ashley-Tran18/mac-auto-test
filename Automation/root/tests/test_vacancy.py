import pytest
from base.base_test import BaseTest
from utils.config_reader import ConfigReader
from pages.vacancy_page import VacancyPage
from pages.login_page import LoginPage
from time import sleep
@pytest.mark.usefixtures("setup")
 
class TestVacancy(BaseTest):
   
    def test_vacancy(self):
        vacancy_page = VacancyPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.login(*ConfigReader.get_username_password())
        self.driver.implicitly_wait(30)
        vacancy_page.click_recruitment_menu()
        vacancy_page.click_vacancy_tag()
        sleep(5)
        vacancy_page.click_add_btn()
        vacancy_page.enter_vacancy_name()
        vacancy_page.choose_job_title()
        sleep(2)
        vacancy_page.enter_description()
        vacancy_page.get_admin_name()
        sleep(2)
        vacancy_page.enter_position()
        vacancy_page.is_active()
        vacancy_page.switch_status_publish()
        vacancy_page.click_save_btn()
        sleep(5)
        edit_text = vacancy_page.check_edit_displayed()
        assert edit_text == "Edit Vacancy"
        vacancy_page.click_cancel_btn()
        sleep(5)
        vacancies_text = vacancy_page.verify_vacancy_again()
        assert vacancies_text == "Vacancies"
        vacancy_page.search_employee()
        vacancy_page.verify_search_result()
        sleep(5)
 
 