import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator
from locators.personal_area_locators import PersonalAreaPageLocator
import time
from data import TestUserData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_assambler(self):
        self.click_on_element(MainPageLocator.ORDERS_FEED_BUTTON)
        self.click_on_element(MainPageLocator.CONSTRUCTOR_BUTTON)

    def check_assambler_text(self):
        return self.get_text_by_element(MainPageLocator.ASSEMBLE_A_BURGER)

    def go_to_order_feed(self):
        self.click_on_element(MainPageLocator.ORDERS_FEED_BUTTON)

    def check_order_feed_text(self):
        return self.get_text_by_element(MainPageLocator.ORDERS_FEED)

    def get_info_ingredient(self):
        self.click_on_element(MainPageLocator.FLUORESCENT_BUN)

    def check_text_about_ingredient(self):
        return self.get_text_by_element(MainPageLocator.INGREDIENT_INFO)

    def close_info_ingredient(self):
        self.click_on_element(MainPageLocator.CLOSE_BUTTON)

    def check_ingredient_info_closed(self):
        return self.wait_and_find_element(MainPageLocator.WINDOW_INFO_INGREDIENT).get_attribute('class')

    def add_bun_to_cart(self, driver):
        actions = ActionChains(driver)
        ingredient = self.wait_and_find_element(MainPageLocator.FLUORESCENT_BUN)
        cart = self.wait_and_find_element(MainPageLocator.CART)
        actions.drag_and_drop(ingredient, cart).perform()

    def login(self):
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON_MAIN)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON)

    def check_order(self):
        self.click_on_element(MainPageLocator.ORDER_BUTTON)
        return self.get_text_by_element(MainPageLocator.ID_ORDER)
    def check_ingredients_counter(self):
        return self.get_text_by_element(MainPageLocator.COUNTER)