from conftest import driver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Messages, UserLogin
from locators import Locators

class TestSignUp:
    def test_sign_up_password_error(self, driver):
        driver.find_element(*Locators.SIGN_UP_FIELD_NAME).send_keys(UserLogin.USER_NAME)
        driver.find_element(*Locators.SIGN_UP_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_UP_FIELD_PASSWORD).send_keys('1')

        driver.find_element(*Locators.SIGN_UP_BUTTON).click()

        sign_up_text_error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SIGN_UP_FIELD_PASSWORD_ERROR)).text
        assert sign_up_text_error == Messages.SIGN_UP_PASSWORD_ERROR



