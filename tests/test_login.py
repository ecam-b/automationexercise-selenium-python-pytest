import pytest

from pages_objects.home_page import HomePage
from pages_objects.login_page import LoginPage
from pages_objects.navbar_page import NavbarPage


class TestLogin:

    @pytest.mark.login
    @pytest.mark.funcional
    def test_login_user_with_correct_email_and_password(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Signup / Login' button
        navbar = NavbarPage(driver)
        navbar.click_signup_link()
        # 5. Verify 'Login to your account' is visible
        login_page = LoginPage(driver)
        assert login_page.is_login_to_your_account_header_displayed(), "El header 'Login to your account' no es visible"
        # 6. Enter correct email address and password
        # 7. Click 'login' button
        login_page.execute_login("sophia.miller_789@example.com", "SecureP@ssw0rd!")
        # 8. Verify that 'Logged in as username' is visible
        assert navbar.is_logged_in_as_user_displayed(), "El usuario no ha iniciado sesión correctamente"
        # 9. Click 'Delete Account' button
        # 10. Verify that 'ACCOUNT DELETED!' is visible
        # En este caso no se elimina la cuenta, ya que es una prueba de inicio de sesión


    @pytest.mark.login
    @pytest.mark.funcional
    def test_login_user_with_incorrect_email_and_password(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Signup / Login' button
        navbar = NavbarPage(driver)
        navbar.click_signup_link()
        # 5. Verify 'Login to your account' is visible
        login_page = LoginPage(driver)
        assert login_page.is_login_to_your_account_header_displayed(), "El header 'Login to your account' no es visible"
        # 6. Enter incorrect email address and password
        # 7. Click 'login' button
        login_page.execute_login("wronEmail@example.com", "wrongPassword123")
        # 8. Verify error 'Your email or password is incorrect!' is visible
        assert login_page.get_error_message() == "your email or password is incorrect!", "El mensaje de error no es el esperado"

    # Logout User
    @pytest.mark.login
    @pytest.mark.funcional
    def test_logout_user(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Signup / Login' button
        navbar = NavbarPage(driver)
        navbar.click_signup_link()
        # 5. Verify 'Login to your account' is visible
        # 5. Verify 'Login to your account' is visible
        login_page = LoginPage(driver)
        assert login_page.is_login_to_your_account_header_displayed(), "El header 'Login to your account' no es visible"
        # 6. Enter correct email address and password
        # 7. Click 'login' button
        login_page.execute_login("sophia.miller_789@example.com", "SecureP@ssw0rd!")
        # 8. Verify that 'Logged in as username' is visible
        assert navbar.is_logged_in_as_user_displayed(), "El usuario no ha iniciado sesión correctamente"
        # 9. Click 'Logout' button
        navbar.click_logout_link()
        # 10. Verify that user is navigated to login page
        assert login_page.is_login_to_your_account_header_displayed(), "El header 'Login to your account' no es visible"
