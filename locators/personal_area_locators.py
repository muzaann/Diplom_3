from selenium.webdriver.common.by import By


class PersonalAreaPageLocator:

    PERSONAL_AREA_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    ACCOUNT = By.XPATH, ".//a[text()='Профиль']"
    INPUT_EMAIL = By.XPATH, ".//label[text()= 'Email']/parent::div/input"
    INPUT_PASSWORD = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"
    AUTH_BUTTON = By.XPATH, "//button[text()= 'Войти']"
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[@href= '/account/order-history']"
    LOGOUT_BUTTON = By.XPATH, "//button[text()= 'Выход']"
    AUTH_BUTTON_MAIN = By.XPATH, ".//button[text()= 'Войти в аккаунт']"

