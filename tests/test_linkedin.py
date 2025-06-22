import time

import pytest


class TestLinkedIn:

    @pytest.mark.debug
    def test_positive_linkedin_login(self, driver):
        driver.get("https://www.linkedin.com/in/elian-camilo-angarita-sanguino/")
        time.sleep(5)