from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants, UserLogin
from locators import Locators

class TestUserProfileExitSuccess:
    def test_user_profile_exit_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.SIGN_IN_URL)

        driver.find_element(*Locators.SIGN_IN_FIELD_EMAIL).send_keys(UserLogin.USER_EMAIL)
        driver.find_element(*Locators.SIGN_IN_FIELD_PASSWORD).send_keys(UserLogin.USER_PASSWORD)

        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.OPEN_USER_PROFILE_LINK))

        driver.find_element(*Locators.OPEN_USER_PROFILE_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.USER_PROFILE_EXIT_BUTTON))

        driver.find_element(*Locators.USER_PROFILE_EXIT_BUTTON).click()
        assert driver.current_url == Constants.SIGN_IN_URL

        driver.quit()