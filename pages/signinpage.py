from .basepage import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    """This class represents SignIn page"""

    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    LOGIN_SUBMIT_BUTTON = (By.ID, "login__submit-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".Common-MessageError-style__message-error___32Yu9")  # noqa

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.send_keys_to_element(email, *self.EMAIL_INPUT)

    def enter_password(self, password):
        self.send_keys_to_element(password, *self.PASSWORD_INPUT)

    def click_login_button(self):
        self.click_element(*self.LOGIN_SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_element_text(*self.ERROR_MESSAGE)
