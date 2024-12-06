from selenium import webdriver

from constants import Constants
from locators import Locators

class TestUseTabsConstructorSuccess:
    def test_use_tabs_souses_constructor_success(self):
        driver = webdriver.Chrome()
        driver.get(Constants.MAIN_PAGE_URL)
        tabs_list = []


        driver.find_element(*Locators.TAB_SOUSES).click()
        tabs_list.append(driver.find_element(*Locators.SOUSE_ELEMENT).text)

        driver.find_element(*Locators.TAB_INGREDIENT).click()
        tabs_list.append(driver.find_element(*Locators.INGREDIENT_ELEMENT).text)

        driver.find_element(*Locators.TAB_BURGER).click()
        tabs_list.append(driver.find_element(*Locators.BURGER_ELEMENT).text)

        assert '0\n90\nСоус Spicy-X' and '0\n1337\nМясо бессмертных моллюсков Protostomia' and '0\n988\nФлюоресцентная булка R2-D3' in tabs_list

        driver.quit()
