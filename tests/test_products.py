import pytest

from pages_objects.home_page import HomePage
from pages_objects.navbar_page import NavbarPage
from pages_objects.product_detail_page import ProductDetailPage
from pages_objects.products_page import ProductsPage


class TestProducts:

    @pytest.mark.products
    @pytest.mark.functional
    def test_verify_all_products_and_product_detail_page(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page is not visible"
        # 4. Click on 'Products' button
        navbar = NavbarPage(driver)
        navbar.click_products_link()
        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        products_page = ProductsPage(driver)
        assert products_page.is_products_page_displayed(), "La pagina de productos no es visible"
        # 6. The products list is visible
        # 7. Click on 'View Product' of first product
        products_page.click_view_first_product_link()
        # 8. User is landed to product detail page
        # 9. Verify that detail is visible: product name, category, price, availability, condition, brand
        details = ProductDetailPage(driver)
        assert details.is_product_details_displayed(), "Los detalles del producto no son visibles"

    @pytest.mark.products
    @pytest.mark.functional
    def test_search_product(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page is not visible"
        # 4. Click on 'Products' button
        navbar = NavbarPage(driver)
        navbar.click_products_link()
        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        products_page = ProductsPage(driver)
        assert products_page.is_products_page_displayed(), "La pagina de productos no es visible"
        # 6. Enter product name in search input and click search button
        products_page.execute_search_product("Blue Top")
        # 7. Verify 'SEARCHED PRODUCTS' is visible
        assert products_page.get_searched_products_header_text() == "searched products", "Searched products header is not visible"
        # 8. Verify all the products related to search are visible
        assert products_page.is_product_item_visible(), "Los productos relacionados con la búsqueda no son visibles"