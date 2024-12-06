from selenium import webdriver

from constants import Constants, UserLogin
from locators import Locators

class TestSignIn:
    def test_sign_in_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.SIGN_IN_URL)

        driver.find_element(*Locators.SIGN_IN_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_IN_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.SIGN_IN_BUTTON).click()

        driver.quit()