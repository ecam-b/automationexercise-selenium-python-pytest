from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class ProductDetailPage(BasePage):
    __product_name_header = (By.CSS_SELECTOR, "div.product-information h2")
    __category_text = (By.XPATH, "//p[contains(text(),'Category')]")
    __price_text = (By.XPATH, "//span[contains(text(),'Rs')]")
    __availability_text = (By.XPATH, "//b[contains(text(),'Availability:')]")
    __condition_text = (By.XPATH, "//b[contains(text(),'Condition:')]")
    __brand_text = (By.XPATH, "//b[contains(text(),'Brand:')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_product_details_displayed(self) -> bool:
        return (super().is_displayed(self.__product_name_header) and
                super().is_displayed(self.__category_text) and
                super().is_displayed(self.__price_text) and
                super().is_displayed(self.__availability_text) and
                super().is_displayed(self.__condition_text) and
                super().is_displayed(self.__brand_text))