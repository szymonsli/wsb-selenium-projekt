from pages.homepage import HomePage
from pages.signinpage import SignInPage
from pages.userspage import UsersPage
from .base_test import BaseTest
from dotenv import load_dotenv
from os import getenv
import selenium.webdriver.support.expected_conditions as EC

load_dotenv()


class TestSignIn(BaseTest):

    def test_sign_in_001(self):
        """User signs in correctly and then logs out"""

        driver = self.driver

        hp = HomePage(driver)
        hp.click_login_button()
        hp.choose_mode("personal")

        sp = SignInPage(driver)
        sp.enter_email(getenv("EMAIL"))
        sp.enter_password(getenv("PASSWORD"))
        sp.click_login_button()

        up = UsersPage(driver)
        up.check_url()
        up.logout()

        assert EC.url_to_be("https://app.nozbe.com/#logout")

    def test_sign_in_002(self):
        """Wrong password
        User is not logged in"""

        driver = self.driver
        hp = HomePage(driver)
        hp.click_login_button()
        hp.choose_mode("personal")

        sp = SignInPage(driver)
        sp.enter_email(getenv("EMAIL"))
        sp.enter_password("wrongpassword")
        sp.click_login_button()
        assert sp.get_error_message() == "Błędne dane"
