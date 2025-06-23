import time

import pytest

from pages_objects.account_created_page import AccountCreatedPage
from pages_objects.delete_account_page import DeleteAccountPage
from pages_objects.home_page import HomePage
from pages_objects.login_page import LoginPage
from pages_objects.navbar_page import NavbarPage
from pages_objects.signup_page import SignupPage


class TestRegister:

    @pytest.mark.register
    @pytest.mark.functional
    def test_register_user(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Signup / Login' button
        navbar = NavbarPage(driver)
        navbar.click_signup_link()
        # 5. Verify 'New User Signup!' is visible
        # 6. Enter name and email address
        # 7. Click 'Signup' button
        login_page = LoginPage(driver)
        login_page.fill_signup_form("Test User", "test-auto41@gmail.com")
        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        signup_page = SignupPage(driver)
        assert signup_page.is_enter_account_info_displayed(), "Signup form header no es visible"
        # 9. Fill details: Title, Name, Email, Password, Date of birth
        # 10. Select checkbox 'Sign up for our newsletter!'
        # 11. Select checkbox 'Receive special offers from our partners!'
        # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        # 13. Click 'Create Account button'
        signup_page.fill_signup_form("TestPassword", "1", "January", "1990",
                                     "Test", "User", "Test Company",
                                     "123 Test St", "Suite 100", "United States",
                                     "California", "Los Angeles", "90001", "1234567890")
        # 14. Verify that 'ACCOUNT CREATED!' is visible
        account_created_page = AccountCreatedPage(driver)
        assert account_created_page.get_header_text() == "account created!", "Account created header no es visible"
        # 15. Click 'Continue' button
        account_created_page.click_continue_button()
        # 16. Verify that 'Logged in as username' is visible
        assert navbar.is_logged_in_as_user_displayed(), "El usuario no ha iniciado sesión correctamente"
        # 17. Click 'Delete Account' button
        navbar.click_delete_account_button()
        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        delete_account_page = DeleteAccountPage(driver)
        assert delete_account_page.get_header_text() == "account deleted!", "En la página de cuenta eliminada no se muestra el mensaje correcto"