import pytest

from pages_objects.contact_us_page import ContactUsPage
from pages_objects.home_page import HomePage
from pages_objects.navbar_page import NavbarPage


class TestContactUs:

    @pytest.mark.contact_us
    @pytest.mark.functional
    def test_contact_us_form(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Contact Us' button
        navbar = NavbarPage(driver)
        navbar.click_contact_us_link()
        # 5. Verify 'GET IN TOUCH' is visible
        contact_us_page = ContactUsPage(driver)
        assert contact_us_page.is_get_in_touch_header_displayed(), "El header 'GET IN TOUCH' no es visible"
        # 6. Enter name, email, subject and message
        # 7. Upload file
        # 8. Click 'Submit' button
        contact_us_page.execute_contact_us_form("Test User", "test@example.com", "Test Subject", "This is a test message.", "user_basic.jpg")
        # 9. Click OK button
        contact_us_page.click_ok_alert_button()
        # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        assert contact_us_page.get_success_message() == "success! your details have been submitted successfully.", "El mensaje de éxito no es el esperado"
        # 11. Click 'Home' button and verify that landed to home page successfully
        navbar.click_home_link()
        assert home_page.is_home_page_displayed(), "No se ha redirigido a la página de inicio correctamente"