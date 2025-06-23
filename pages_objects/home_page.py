from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class HomePage(BasePage):
    _url = "https://automationexercise.com/"
    __home_page_header = (By.XPATH, "//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")
    __subscription_header = (By.CSS_SELECTOR, "div.single-widget h2")
    __email_field = (By.ID, "susbscribe_email")
    __submit_subscription_button = (By.ID, "subscribe")
    __subscription_alert = (By.CSS_SELECTOR, "div.alert-success.alert")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def is_home_page_displayed(self) -> bool:
        return super().is_displayed(self.__home_page_header)

    def is_subscription_header_displayed(self) -> bool:
        return super().is_displayed(self.__subscription_header)

    def execute_subscription(self, email: str):
        super()._type(self.__email_field, email)
        super()._click(self.__submit_subscription_button)

    def is_subscription_alert_displayed(self) -> bool:
        return super().is_displayed(self.__subscription_alert)