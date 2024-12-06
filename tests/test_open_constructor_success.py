from selenium import webdriver

from constants import Constants
from locators import Locators


class TestOpenConstructorSuccess:
    def test_open_constructor_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.MAIN_PAGE_URL)

        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        assert driver.current_url == Constants.CONSTRUCTOR_PAGE_URL

        driver.quit()

    def test_open_constructor_by_logo_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.MAIN_PAGE_URL)

        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()

        assert driver.current_url == Constants.CONSTRUCTOR_PAGE_URL

        driver.quit()