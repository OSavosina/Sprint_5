import pytest
from selenium import webdriver

from constants import Constants


@pytest.fixture(scope="module", params=[
    Constants.SIGN_UP_URL,
    Constants.SIGN_IN_URL,
    Constants.CONSTRUCTOR_PAGE_URL,
    Constants.MAIN_PAGE_URL,
    Constants.FORGOT_PASSWORD_URL,
    Constants.USER_PROFILE_PAGE_URL
])
def driver(request):
    browser = webdriver.Chrome()
    browser.get(request.param)
    yield browser
    browser.quit()

