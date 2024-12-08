from conftest import driver

from constants import Constants
from locators import Locators

class TestOpenFormSignInSuccess:
    def test_open_form_sign_in_by_button_enter_success(self, driver):

        driver.find_element(*Locators.ENTER_TO_LOGIN_BUTTON).click()
        assert driver.current_url == Constants.SIGN_IN_URL


    def test_open_form_sign_in_by_button_lk_success(self, driver):
        driver.find_element(*Locators.OPEN_USER_PROFILE_BUTTON).click()
        assert driver.current_url == Constants.SIGN_IN_URL


    def test_open_form_sign_in_from_sign_up_page_success(self, driver):
        driver.find_element(*Locators.OPEN_USER_PROFILE_LINK).click()
        assert driver.current_url == Constants.SIGN_IN_URL


    def test_open_form_sign_in_from_forgot_password_page_success(self, driver):
        driver.find_element(*Locators.OPEN_USER_PROFILE_LINK).click()
        assert driver.current_url == Constants.SIGN_IN_URL
