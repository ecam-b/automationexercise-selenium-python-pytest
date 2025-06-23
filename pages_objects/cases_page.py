from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class CasesPage(BasePage):
    __test_cases_header = (By.TAG_NAME, "h2")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_test_cases_page_displayed(self) -> bool:
        return super().is_displayed(self.__test_cases_header)