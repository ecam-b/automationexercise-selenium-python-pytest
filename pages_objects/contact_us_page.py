from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class ContactUsPage(BasePage):
    __get_in_touch_header = (By.CSS_SELECTOR, "div.contact-form h2")
    __name_field = (By.NAME, "name")
    __email_field = (By.NAME, "email")
    __subject_field = (By.NAME, "subject")
    __message_field = (By.ID, "message")
    __upload_field = (By.NAME, "upload_file")
    __message_success = (By.CSS_SELECTOR, "div.contact-form div.status")

    __submit_button = (By.XPATH, "//input[@data-qa='submit-button']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_get_in_touch_header_displayed(self) -> bool:
        return super().is_displayed(self.__get_in_touch_header)

    def execute_contact_us_form(self, name: str, email: str, subject: str, message: str, file_name: str = "user_basic.jpg"):
        super()._type(self.__name_field, name)
        super()._type(self.__email_field, email)
        super()._type(self.__subject_field, subject)
        super()._type(self.__message_field, message)
        super()._select_file(self.__upload_field, file_name)
        super()._click(self.__submit_button)

    def click_ok_alert_button(self):
        super()._accept_alert()

    def get_success_message(self) -> str:
        return super()._get_text(self.__message_success)