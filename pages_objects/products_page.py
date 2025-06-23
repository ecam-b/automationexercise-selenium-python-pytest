from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages_objects.base_page import BasePage


class ProductsPage(BasePage):
    __all_products_header = (By.CSS_SELECTOR, "div.features_items h2.title")
    __view_first_product_link = (By.XPATH, "//a[@href='/product_details/1']")
    __search_product_input = (By.ID, "search_product")
    __search_button = (By.ID, "submit_search")
    __searched_products_header = (By.CSS_SELECTOR, "div.features_items h2.title")
    __product_item = (By.CSS_SELECTOR, "div.single-products")
    __add_to_cart_button = (By.CSS_SELECTOR, "div.overlay-content a.add-to-cart")
    __continue_shopping_button = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    __view_cart_link = (By.PARTIAL_LINK_TEXT, "View Cart")

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

    def add_product_to_cart_by_index(self, product_index: int):
        """
        Añade un producto al carrito por su índice (posición) en la lista de productos.
        El índice es 1-basado (el primer producto es 1).
        """
        products: list[WebElement] = self._find_all(self.__product_item)

        if product_index > len(products):
            raise IndexError(
                f"Índice de producto fuera de rango. Hay {len(products)} productos, pero se solicitó el índice {product_index}.")

        product_to_interact_with = products[product_index - 1]
        super()._scroll_to_element(product_to_interact_with)
        super()._hover_over_element(product_to_interact_with)
        # Encontrar el botón "Add to cart" dentro del producto seleccionado
        add_to_cart_button = product_to_interact_with.find_element(*self.__add_to_cart_button)
        add_to_cart_button.click()

    def click_continue_shopping_button(self):
        super()._click(self.__continue_shopping_button)

    def click_view_cart_link(self):
        super()._click(self.__view_cart_link)