from selenium.webdriver.common.by import By


class PersonalAreaPageLocator:

    PERSONAL_AREA_BUTTON = By.XPATH, "/html/body/div/div/header/nav/a/p"
    ACCOUNT = By.XPATH, ".//a[text()='Профиль']"
    INPUT_EMAIL = By.XPATH, ".//label[text()= 'Email']/parent::div/input"  # Email при авторизации
    INPUT_PASSWORD = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"  # Пароль при авторизации
    AUTH_BUTTON = By.XPATH, "//button[text()= 'Войти']"
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[@href= '/account/order-history']"
    LOGOUT_BUTTON = By.XPATH, "//button[text()= 'Выход']"
    ALL_PAGE = By.XPATH, "/html"
    AUTH_BUTTON_MAIN = By.XPATH, ".//button[text()= 'Войти в аккаунт']"
    LOADING_WINDOW = By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"