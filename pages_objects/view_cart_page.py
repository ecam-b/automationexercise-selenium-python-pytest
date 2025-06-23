from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class ViewCartPage(BasePage):
    __first_product = (By.ID, "product-1")
    __prince_value = (By.CSS_SELECTOR, "td.cart_price p")
    __quantity_value = (By.CSS_SELECTOR, "td.cart_quantity button")
    __total_price_value = (By.CSS_SELECTOR, "td.cart_total p")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_any_product_in_cart(self) -> bool:
        return super().is_displayed(self.__first_product)

    def is_details_of_first_product_displayed(self) -> bool:
        return (super().is_displayed(self.__prince_value) and
                super().is_displayed(self.__quantity_value) and
                super().is_displayed(self.__total_price_value))