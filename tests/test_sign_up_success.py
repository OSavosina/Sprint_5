from selenium import webdriver

from constants import Constants, UserLogin
from locators import Locators

class TestSignUp:
    def test_sign_up_password_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.SIGN_UP_URL)

        driver.find_element(*Locators.SIGN_UP_FIELD_NAME).send_keys(UserLogin.USER_NAME)
        driver.find_element(*Locators.SIGN_UP_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_UP_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.SIGN_UP_BUTTON).click()

        driver.quit()