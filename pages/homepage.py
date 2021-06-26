from .basepage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """This class represents homepage"""

    LOGIN_BUTTON = (By.ID, "login-button")
    PERSONAL_MODE_BUTTON = (By.XPATH, '(//a[contains(@class, "bg-green")])[2]')
    TEAMS_MODE_BUTTON = (By.XPATH, '(//a[contains(@class, "bg-purple")])[3]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)

    def choose_mode(self, mode="personal"):
        if mode == "personal":
            self.click_element(*self.PERSONAL_MODE_BUTTON)
        else:
            self.click_element(*self.TEAMS_MODE_BUTTON)
