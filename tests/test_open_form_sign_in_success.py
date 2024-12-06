from selenium import webdriver

from constants import Constants
from locators import Locators

class TestOpenFormSignInSuccess:
    def test_open_form_sign_in_by_button_enter_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.MAIN_PAGE_URL)

        driver.find_element(*Locators.ENTER_TO_LOGIN_BUTTON).click()
        assert driver.current_url == Constants.SIGN_IN_URL

        driver.quit()

    def test_open_form_sign_in_by_button_lk_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.MAIN_PAGE_URL)

        driver.find_element(*Locators.OPEN_USER_PROFILE_BUTTON).click()
        assert driver.current_url == Constants.SIGN_IN_URL

        driver.quit()

    def test_open_form_sign_in_from_sign_up_page_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.SIGN_UP_URL)

        driver.find_element(*Locators.OPEN_USER_PROFILE_LINK).click()
        assert driver.current_url == Constants.SIGN_IN_URL

        driver.quit()

    def test_open_form_sign_in_from_forgot_password_page_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.FORGOT_PASSWORD_URL)

        driver.find_element(*Locators.OPEN_USER_PROFILE_LINK).click()
        assert driver.current_url == Constants.SIGN_IN_URL

        driver.quit()