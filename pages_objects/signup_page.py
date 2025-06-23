from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class SignupPage(BasePage):
    __signup_form_header = (By.CSS_SELECTOR, "div h2.title.text-center")
    __mr_checkbox = (By.ID, "id_gender1")
    __password_field = (By.ID, "password")
    __day_dropdown = (By.ID, "days")
    __month_dropdown = (By.ID, "months")
    __year_dropdown = (By.ID, "years")
    __newsletter_checkbox = (By.ID, "newsletter")
    __special_offers_checkbox = (By.ID, "optin")
    __first_name_field = (By.ID, "first_name")
    __last_name_field = (By.ID, "last_name")
    __company_field = (By.ID, "company")
    __address1_field = (By.ID, "address1")
    __address2_field = (By.ID, "address2")
    __country_dropdown = (By.ID, "country")
    __state_field = (By.ID, "state")
    __city_field = (By.ID, "city")
    __zipcode_field = (By.ID, "zipcode")
    __mobile_number_field = (By.ID, "mobile_number")
    __create_account_button = (By.XPATH, "//button[@data-qa='create-account']")



    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_enter_account_info_displayed(self) -> bool:
        return super().is_displayed(self.__signup_form_header)

    def fill_signup_form(self, password: str, day: str, month: str, year: str,
                        first_name: str, last_name: str, company: str, address1: str,
                        address2: str, country: str, state: str, city: str,
                        zipcode: str, mobile_number: str):
        super()._click(self.__mr_checkbox)
        super()._type(self.__password_field, password)
        super()._select_dropdown_by_visible_text(self.__day_dropdown, day)
        super()._select_dropdown_by_visible_text(self.__month_dropdown, month)
        super()._select_dropdown_by_visible_text(self.__year_dropdown, year)
        super()._click(self.__newsletter_checkbox)
        super()._click(self.__special_offers_checkbox)
        super()._type(self.__first_name_field, first_name)
        super()._type(self.__last_name_field, last_name)
        super()._type(self.__company_field, company)
        super()._type(self.__address1_field, address1)
        super()._type(self.__address2_field, address2)
        super()._select_dropdown_by_visible_text(self.__country_dropdown, country)
        super()._type(self.__state_field, state)
        super()._type(self.__city_field, city)
        super()._type(self.__zipcode_field, zipcode)
        super()._type(self.__mobile_number_field, mobile_number)
        super()._click(self.__create_account_button)
