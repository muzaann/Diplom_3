from selenium.webdriver.common.by import By

class LoginPageLocator:

    PERSONAL_AREA_BUTTON = By.XPATH, "/html/body/div/div/header/nav/a/p"
    EYE_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon-action')]"
    NEW_PASSWORD_FIELD = By.XPATH, ".//label[text()='Пароль']"
    RECOVERY_PASSWORD_BLOCK = By.XPATH, "//*[contains(@class, 'button_button') and text()='Восстановить']"
    RECOVERY_PASSWORD_BUTTON = By.XPATH, "//*[@href= '/forgot-password']"
    DZEN_LOGO_BUTTON_LOCATOR = By.XPATH, "//*[@href= '///forgot-password']"
    TEXT_SCOOTER = By.XPATH, "//*[contains(@class, 'Home_Header')]"
    WINDOW_TEXT = By.XPATH, "//*[@title= 'Установить']"
    ClOSE_WINDOWS_BUTTON = By.TAG_NAME, "polygon"
    SEARCH_DZEN_BUTTON = By.ID, "dzen-header"
    PERSONAL_AREA = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/account']"  # Личный кабинет
    REGISTRATION = By.XPATH, ".//a[contains(@class, 'Auth_link') and @href= '/register']"  # Зарегестрироваться
    REGISTRATION_NAME = By.XPATH, ".//label[text()= 'Имя']/parent::div/input"  # Имя при регистрации
    REGISTRATION_EMAIL = By.XPATH, ".//label[text()= 'Email']/parent::div/input"  # Email при регистрации
    REGISTRATION_PASSWORD = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"  # Пароль при регистрации
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()= 'Зарегистрироваться']"  # Кнопка зарегистрироваться
    ACCOUNT_EXIT = By.XPATH, "//button[text()= 'Выход']"
    PASSWORD_RECOVERY_FIELD = By.XPATH, "//input[@name= 'name']"
    PASSWORD_RECOVERY_BUTTON = By.XPATH, "//button[text()= 'Восстановить']"
    CODE_FROM_EMAIL = By.XPATH, ".//label[text()= 'Введите код из письма']"
