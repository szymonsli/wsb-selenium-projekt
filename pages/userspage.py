from .basepage import BasePage
from selenium.webdriver.common.by import By


class UsersPage(BasePage):
    """This class represents Users page"""

    SETTINGS = (By.ID, "icobar__settings")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Wyloguj")

    def __init__(self, driver):
        super().__init__(driver)

    def open_settings(self):
        self.click_element(*self.SETTINGS)

    def logout(self):
        self.click_element(*self.SETTINGS)
        self.click_element(*self.LOGOUT_BUTTON)

    def check_url(self):
        return self.be_url("https://app.nozbe.com/#na")
