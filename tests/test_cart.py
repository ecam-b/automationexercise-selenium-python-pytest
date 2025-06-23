from pages_objects.home_page import HomePage
from pages_objects.navbar_page import NavbarPage
from pages_objects.products_page import ProductsPage
from pages_objects.view_cart_page import ViewCartPage


class TestCart:

    # Add Products in Cart
    def test_add_products_in_cart(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page is not visible"
        # 4. Click on 'Products' button
        navbar = NavbarPage(driver)
        navbar.click_products_link()
        # 5. Hover over first product and click 'Add to cart'
        products_page = ProductsPage(driver)
        products_page.add_product_to_cart_by_index(1)
        # 6. Click 'Continue Shopping' button
        products_page.click_continue_shopping_button()
        # 7. Hover over second product and click 'Add to cart'
        products_page.add_product_to_cart_by_index(10)
        # 8. Click 'View Cart' button
        products_page.click_view_cart_link()
        # 9. Verify both products are added to Cart
        view_cart_page = ViewCartPage(driver)
        assert view_cart_page.is_any_product_in_cart(), "No hay productos en el carrito"
        # 10. Verify their prices, quantity and total price
        assert view_cart_page.is_details_of_first_product_displayed(), "Los detalles del primer producto no están visibles"