from conftest import driver

from constants import Constants, UserLogin
from locators import Locators


class TestOpenForgotPasswordPageSuccess:
    def test_open_forgot_password_page_success(self, driver):
        driver.find_element(*Locators.SIGN_UP_FIELD_NAME).send_keys(UserLogin.USER_NAME)
        driver.find_element(*Locators.SIGN_UP_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_UP_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.OPEN_USER_PROFILE_BUTTON).click()
        driver.get(Constants.FORGOT_PASSWORD_URL)
        assert driver.current_url == Constants.FORGOT_PASSWORD_URL
