from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.wait_and_find_element(locator).click()

    def wait_invisible(self, locator, value):
        self.wait_and_find_element(locator)
        return WebDriverWait(self.driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, value))

    def get_text_by_element(self, locator):
        return self.wait_and_find_element(locator).text

    def set_text_to_element(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    def switch_to_window(self, window):
        return self.driver.switch_to.window(self.driver.window_handles[window])

    def scroll_and_click_with_wait(self, locator):
        self.scroll_to_element(locator)
        self.wait_and_find_element(locator)
        self.click_on_element(locator)

    def scroll_and_find_element(self, locator):
        self.scroll_to_element(locator)
        self.wait_and_find_element(locator)


