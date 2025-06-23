from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class LoginPage(BasePage):
    __name_signup_field = (By.NAME, "name")
    __email_signup_field = (By.XPATH, "//input[@data-qa='signup-email']")
    __signup_button = (By.XPATH, "//button[@data-qa='signup-button']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def fill_signup_form(self, name: str, email: str):
        super()._type(self.__name_signup_field, name)
        super()._type(self.__email_signup_field, email)
        super()._click(self.__signup_button)