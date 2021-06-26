import pytest
from selenium import webdriver

BASE_URL = "https://nozbe.com/pl/"


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # SETUP
        self.driver = webdriver.Firefox()
        self.driver.get(BASE_URL)
        assert "Nozbe" in self.driver.title
        yield self.driver

        # TEARDOWN
        self.driver.close()
