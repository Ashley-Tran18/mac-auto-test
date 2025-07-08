# base/base_test.py

from selenium import webdriver
from utils.config_reader import ConfigReader
import pytest
import allure


class BaseTest:
    # Hook để lưu kết quả từng giai đoạn test (setup/call/teardown)
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        # This hook is used to capture the outcome of the test
        outcome = yield
        rep = outcome.get_result()
        setattr(item, f"rep_{rep.when}", rep)


    @pytest.fixture(autouse=True)
    def setup(self,request):
        self.driver = webdriver.Chrome()  
        self.driver.get(ConfigReader.get_base_url())
    
        self.driver.maximize_window()
        request.cls.driver = self.driver

        yield
        # Chỉ chụp screenshot nếu phần thực thi test (`call`) bị fail
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            print("Go HERE")
            
            try:
                self.driver.save_screenshot(f"screenshot_{request.node.name}.png")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=f"failure_{request.node.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                print("Attaching screenshot for test:", request.node.name)
            except Exception as e:
                 print(f"Could not capture screenshot: {e}")
        self.driver.quit()
        