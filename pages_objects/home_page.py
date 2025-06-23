from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class HomePage(BasePage):
    _url = "https://automationexercise.com/"
    __home_page_header = (By.XPATH, "//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def is_home_page_displayed(self) -> bool:
        return super().is_displayed(self.__home_page_header)