from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class NavbarPage(BasePage):
    __signup_link = (By.PARTIAL_LINK_TEXT, "Signup")
    __logged_is_as_user_link = (By.PARTIAL_LINK_TEXT, "Logged in as")
    __delete_account_link = (By.PARTIAL_LINK_TEXT, "Delete Account")
    __logout_link = (By.PARTIAL_LINK_TEXT, "Logout")
    __contact_us_link = (By.PARTIAL_LINK_TEXT, "Contact us")
    __home_link = (By.PARTIAL_LINK_TEXT, "Home")

    def __init__(self, driver : WebDriver):
        super().__init__(driver)

    def click_signup_link(self):
        super()._click(self.__signup_link)

    def is_logged_in_as_user_displayed(self) -> bool:
        return super().is_displayed(self.__logged_is_as_user_link)

    def click_delete_account_link(self):
        super()._click(self.__delete_account_link)

    def click_logout_link(self):
        super()._click(self.__logout_link)

    def click_contact_us_link(self):
        super()._click(self.__contact_us_link)

    def click_home_link(self):
        super()._click(self.__home_link)