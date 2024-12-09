from conftest import driver

from constants import UserLogin
from locators import Locators

class TestSignIn:
    def test_sign_in_success(self, driver):
        driver.find_element(*Locators.SIGN_IN_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_IN_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
