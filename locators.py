from selenium.webdriver.common.by import By


class Locators:
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    SIGN_UP_FIELD_NAME = (By.XPATH,"//label[contains(text(), 'Имя')]/following::*[starts-with(name(), 'input')]")
    SIGN_UP_FIELD_EMAIL = (By.XPATH,"//label[contains(text(), 'Email')]/following::*[starts-with(name(), 'input')]")
    SIGN_UP_FIELD_PASSWORD = (By.XPATH,"//label[contains(text(), 'Пароль')]/following::*[starts-with(name(), 'input')]")
    SIGN_UP_FIELD_PASSWORD_ERROR = (By.XPATH,"//label[contains(text(), 'Пароль')]/following::p[contains(text(), 'Некорректный пароль')]")


    ENTER_TO_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    OPEN_USER_PROFILE_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
    OPEN_USER_PROFILE_LINK = (By.XPATH, "//a[@href='/login']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a[1]")
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")
    USER_PROFILE_EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    TAB_BURGER = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")
    TAB_SOUSES = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    TAB_INGREDIENT = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")
    BURGER_ELEMENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]/parent::a")
    SOUSE_ELEMENT = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]/parent::a")
    INGREDIENT_ELEMENT = (By.XPATH, "//p[contains(text(), 'Мясо бессмертных моллюсков Protostomia')]/parent::a")

    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    SIGN_IN_FIELD_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following::*[starts-with(name(), 'input')][1]")
    SIGN_IN_FIELD_PASSWORD = (By.XPATH, "//label[contains(text(), 'Пароль')]/following::*[starts-with(name(), 'input')]")
