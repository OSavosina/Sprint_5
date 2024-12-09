from conftest import driver

from constants import Constants
from locators import Locators


class TestOpenConstructorSuccess:
    def test_open_constructor_success(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        assert driver.current_url == Constants.CONSTRUCTOR_PAGE_URL


    def test_open_constructor_by_logo_success(self, driver):
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()

        assert driver.current_url == Constants.CONSTRUCTOR_PAGE_URL
