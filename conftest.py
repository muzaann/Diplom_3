import pytest
from selenium import webdriver



@pytest.fixture()
def driver_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--width=1080")
    firefox_options.add_argument("--height=800")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture()
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1280,800')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

