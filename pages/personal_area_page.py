import allure
from pages.base_page import BasePage
from locators.personal_area_locators import PersonalAreaPageLocator
import time
from data import TestUserData


class PersonalAreaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Переходим на страницу восстановления пароля, вводит e-mail, кликаем на кнопку \
                               "Восстановить", проверяем появление поля "Введите код из письма"')
    def go_to_personal_area_with_auth(self):
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON_MAIN)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAreaPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAreaPageLocator.AUTH_BUTTON)
        self.click_on_element(PersonalAreaPageLocator.PERSONAL_AREA_BUTTON)

    def check_text_on_button_profile(self):
        # time.sleep(3)
        return self.get_text_by_element(PersonalAreaPageLocator.ACCOUNT)

    def check_history_orders(self):
        # time.sleep(3)
        self.click_on_element(PersonalAreaPageLocator.ORDERS_HISTORY_BUTTON)
        return self.get_text_by_element(PersonalAreaPageLocator.ORDERS_HISTORY_BUTTON)

    def check_logout(self):
        # time.sleep(3)
        self.click_on_element(PersonalAreaPageLocator.LOGOUT_BUTTON)
        return self.get_text_by_element(PersonalAreaPageLocator.AUTH_BUTTON)
