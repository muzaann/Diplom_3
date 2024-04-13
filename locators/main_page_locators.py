from selenium.webdriver.common.by import By


class MainPageLocator:
    CONSTRUCTOR_BUTTON = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/']"
    ASSEMBLE_A_BURGER = By.XPATH, ".//h1[text()='Соберите бургер']"
    ORDERS_FEED_BUTTON = By.XPATH, ".//p[text()= 'Лента Заказов']"
    ORDERS_FEED = By.XPATH, ".//h1[text()= 'Лента заказов']"
    FLUORESCENT_BUN = By.XPATH, "//p[text()= 'Флюоресцентная булка R2-D3']"
    INGREDIENT_INFO = By.XPATH, ".//h2[text()= 'Детали ингредиента']"
    CLOSE_BUTTON = By.XPATH, ".//button[@type='button']"
    WINDOW_INFO_INGREDIENT = By.XPATH, "//section[contains(@class, 'Modal_modal')]"
    CART = By.XPATH, "//span[text()= 'Перетяните булочку сюда (верх)']"
    COUNTER = By.XPATH, "//a[@href= '/ingredient/61c0c5a71d1f82001bdaaa6d']/div/p[contains(@class, 'counter')]"
    ORDER_BUTTON = By.XPATH, "//button[text()= 'Оформить заказ']"
    ID_ORDER = By.XPATH, "//p[text()= 'идентификатор заказа']"


