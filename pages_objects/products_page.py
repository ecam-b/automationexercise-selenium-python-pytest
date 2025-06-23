from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages_objects.base_page import BasePage


class ProductsPage(BasePage):
    __all_products_header = (By.CSS_SELECTOR, "div.features_items h2.title")
    __view_first_product_link = (By.XPATH, "//a[@href='/product_details/1']")
    __search_product_input = (By.ID, "search_product")
    __search_button = (By.ID, "submit_search")
    __searched_products_header = (By.CSS_SELECTOR, "div.features_items h2.title")
    __product_item = (By.CSS_SELECTOR, "div.single-products")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_products_page_displayed(self) -> bool:
        return super().is_displayed(self.__all_products_header)

    def click_view_first_product_link(self):
        super()._click(self.__view_first_product_link)

    def execute_search_product(self, product_name: str):
        super()._type(self.__search_product_input, product_name)
        super()._click(self.__search_button)

    def get_searched_products_header_text(self) -> str:
        return super()._get_text(self.__searched_products_header)

    def is_product_item_visible(self) -> bool:
        return super().is_displayed(self.__product_item)