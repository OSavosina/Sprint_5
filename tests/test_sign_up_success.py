from conftest import driver

from constants import UserLogin
from locators import Locators

class TestSignUp:
    def test_sign_up_password_success(self, driver):
        driver.find_element(*Locators.SIGN_UP_FIELD_NAME).send_keys(UserLogin.USER_NAME)
        driver.find_element(*Locators.SIGN_UP_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_UP_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
