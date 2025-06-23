from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class DeleteAccountPage(BasePage):
    __header_account_deleted = (By.XPATH, "//h2[@data-qa='account-deleted']")
    __continue_button = (By.XPATH, "//a[@data-qa='continue-button']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        return super()._get_text(self.__header_account_deleted)

    def click_continue_button(self):
        super()._click(self.__continue_button)
