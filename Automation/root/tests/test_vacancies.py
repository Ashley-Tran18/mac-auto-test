from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage
from utils.config_reader import ConfigReader
import allure

class TestVacancies(BaseTest):
    @allure.story("Add Vacancy Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_recruitment_navigation(self):
        login_page = LoginPage(self.driver)
        login_page.login(*ConfigReader.get_username_password())

        vacancies_page = VacanciesPage(self.driver)  # truyền driver từ BaseTest
        vacancies_page.navigate_to_recruitment()  # gọi hàm để test navigation
        vacancies_page.navigate_to_vacancies()
        vacancies_page.click_add_button()

        # vacancy_data = ConfigReader.get_vacancy_info()
        # vacancies_page.add_vacancy(vacancy_data)
        vacancies_page.add_vacancy(ConfigReader.get_vacancy_info())
        vacancies_page.select_job_title(ConfigReader.get_vacancy_info())
        vacancies_page.input_description(ConfigReader.get_vacancy_info())
        vacancies_page.select_hiring_manager()
        vacancies_page.input_position(ConfigReader.get_vacancy_info())
        vacancies_page.check_toggle()
        
        # assert vacancies_page.is_vacancy_added_successfully() == "Successfully Saved"

        # edit_text = vacancies_page.is_edit_header_display()
        # assert edit_text == "Edit Vacancy"
        assert vacancies_page.is_edit_header_display() == "Edit Vacancy"

        vacancies_page.cancel_edit()

        assert vacancies_page.verify_vacancy_page_display() == "Vacancies"

        vacancies_page.filter_vacancy(ConfigReader.get_vacancy_info())