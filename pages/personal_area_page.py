import allure
from pages.base_page import BasePage
from locators.personal_area_locators import PersonalAreaPageLocator
from data import TestUserData


class PersonalAreaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Авторизация и переход в личный кабинет')
    def go_to_personal_area_with_auth(self):
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON_MAIN)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON)
        self.click_on_element(PersonalAreaPageLocator.PERSONAL_AREA_BUTTON)

    @allure.step('Получение текста по локатору "Профиль" в личном кабинете')
    def check_text_on_button_profile(self):
        return self.get_text_by_element(PersonalAreaPageLocator.ACCOUNT)

    @allure.step('Переход и получение текста по локтору "История заказов')
    def check_history_orders(self):
        self.click_on_element(PersonalAreaPageLocator.ORDERS_HISTORY_BUTTON)
        return self.get_text_by_element(PersonalAreaPageLocator.ORDERS_HISTORY_BUTTON)

    @allure.step('Выход из Личного кабинета и получение текста на кнопку входа')
    def check_logout(self):
        self.click_on_element(PersonalAreaPageLocator.LOGOUT_BUTTON)
        return self.get_text_by_element(PersonalAreaPageLocator.AUTH_BUTTON)
