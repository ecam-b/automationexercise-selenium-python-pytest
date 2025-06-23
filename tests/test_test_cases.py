import pytest

from pages_objects.cases_page import CasesPage
from pages_objects.home_page import HomePage
from pages_objects.navbar_page import NavbarPage


class TestTestCases:

    @pytest.mark.test_cases
    @pytest.mark.functional
    def test_test_cases_page(self, driver):
        # 1. Launch browser
        home_page = HomePage(driver)
        # 2. Navigate to url 'http://automationexercise.com'
        home_page.open()
        # 3. Verify that home page is visible successfully
        assert home_page.is_home_page_displayed(), "Home page no es visible"
        # 4. Click on 'Test Cases' button
        navbar = NavbarPage(driver)
        navbar.click_test_cases_link()
        # 5. Verify user is navigated to test cases page successfully
        test_cases_page = CasesPage(driver)
        assert test_cases_page.is_test_cases_page_displayed(), "Test cases page no es visible"
