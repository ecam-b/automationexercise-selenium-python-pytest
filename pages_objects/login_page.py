from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class LoginPage(BasePage):
    __new_user_signup_header = (By.CSS_SELECTOR, "div.signup-form h2")
    __name_signup_field = (By.NAME, "name")
    __email_signup_field = (By.XPATH, "//input[@data-qa='signup-email']")
    __signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    __signup_error_message = (By.CSS_SELECTOR, "div.signup-form p")
    __login_to_your_account_header = (By.CSS_SELECTOR, "div.login-form h2")
    __email_login_field = (By.XPATH, "//input[@data-qa='login-email']")
    __password_login_field = (By.XPATH, "//input[@data-qa='login-password']")
    __login_button = (By.XPATH, "//button[@data-qa='login-button']")
    __login_error_message = (By.CSS_SELECTOR, "div.login-form p")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_new_user_signup_header_displayed(self) -> bool:
        return super().is_displayed(self.__new_user_signup_header)

    def execute_signup_form(self, name: str, email: str):
        super()._type(self.__name_signup_field, name)
        super()._type(self.__email_signup_field, email)
        super()._click(self.__signup_button)

    def get_signup_error_message(self) -> str:
        return super()._get_text(self.__signup_error_message)

    def is_login_to_your_account_header_displayed(self) -> bool:
        return super().is_displayed(self.__login_to_your_account_header)

    def execute_login_form(self, email: str, password: str):
        super()._type(self.__email_login_field, email)
        super()._type(self.__password_login_field, password)
        super()._click(self.__login_button)

    def get_login_error_message(self) -> str:
        return super()._get_text(self.__login_error_message)
