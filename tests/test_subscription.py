import pytest

from pages_objects.home_page import HomePage
from pages_objects.navbar_page import NavbarPage


class TestSubcription:

    @pytest.mark.subcription
    @pytest.mark.functional
    def test_verify_subscription(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Scroll down to footer
        # 5. Verify text 'SUBSCRIPTION'
        assert home_page.is_subscription_header_displayed(), "El header de suscripción no es visible"
        # 6. Enter email address in input and click arrow button
        home_page.execute_subscription("sophia.miller_789@example.com")
        # 7. Verify success message 'You have been successfully subscribed!' is visible
        assert home_page.is_subscription_alert_displayed(), "El mensaje de suscripción no es visible"

    @pytest.mark.subcription
    @pytest.mark.functional
    def test_verify_subscription_in_cart(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click 'Cart' button
        navbar = NavbarPage(driver)
        navbar.click_cart_link()
        # 5. Scroll down to footer
        # 6. Verify text 'SUBSCRIPTION'
        assert home_page.is_subscription_header_displayed(), "El header de suscripción no es visible"
        # 7. Enter email address in input and click arrow button
        home_page.execute_subscription("sophia.miller_789@example.com")
        # 8. Verify success message 'You have been successfully subscribed!' is visible
        assert home_page.is_subscription_alert_displayed(), "El mensaje de suscripción no es visible"
