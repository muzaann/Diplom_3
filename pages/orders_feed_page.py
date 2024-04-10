import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersPageLocator
from locators.personal_area_locators import PersonalAreaPageLocator
from locators.main_page_locators import MainPageLocator
import time
from data import TestUserData


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_order_feed(self):
        self.click_on_element(OrdersPageLocator.ORDERS_FEED_BUTTON)

    def get_order_info(self):
        self.click_on_element(OrdersPageLocator.ORDER_1)
        return self.get_text_by_element(OrdersPageLocator.ORDER_INFO)

    def login(self):
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON_MAIN)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON)

    def create_order(self, driver):
        actions = ActionChains(driver)
        ingredient = self.wait_and_find_element(MainPageLocator.FLUORESCENT_BUN)
        cart = self.wait_and_find_element(MainPageLocator.CART)
        actions.drag_and_drop(ingredient, cart).perform()
        self.click_on_element(MainPageLocator.ORDER_BUTTON)

    def go_to_constructor(self):
        self.click_on_element(OrdersPageLocator.CONSTRUCTOR_BUTTON)


    def get_order_number(self):
        self.wait_invisible(OrdersPageLocator.ID_NEW_ORDER, '9999')
        return self.get_text_by_element(OrdersPageLocator.ID_NEW_ORDER)

    def get_orders_numbers(self):
        self.click_on_element(OrdersPageLocator.CLOSE_BUTTON)
        self.click_on_element(OrdersPageLocator.ORDERS_FEED_BUTTON)
        return self.get_text_by_element(OrdersPageLocator.ORDERS_NUMBERS)

    def go_to_orders_feed_from_order_info(self):
        self.click_on_element(OrdersPageLocator.CLOSE_BUTTON)
        self.click_on_element(OrdersPageLocator.ORDERS_FEED_BUTTON)

    def get_count_all_time(self):
        return self.get_text_by_element(OrdersPageLocator.COUNTER_ALL_TIME)

    def get_count_today(self):
        return self.get_text_by_element(OrdersPageLocator.COUNTER_TODAY)

    def get_orders_in_work(self):
        self.click_on_element(OrdersPageLocator.CLOSE_BUTTON)
        self.click_on_element(OrdersPageLocator.ORDERS_FEED_BUTTON)
        self.wait_invisible(OrdersPageLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!')
        return self.get_text_by_element(OrdersPageLocator.ORDERS_IN_WORK)


