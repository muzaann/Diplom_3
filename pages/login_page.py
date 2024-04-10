import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator
import time
from data import TestUserData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # @allure.step ('Клик по лого "Самокат" из окна оформления заказа')
    def go_to_recovery_page(self):
        time.sleep(5)
        self.click_on_element(LoginPageLocator.PERSONAL_AREA_BUTTON)
        self.click_on_element(LoginPageLocator.RECOVERY_PASSWORD_BUTTON)

    # @allure.step ('Проверка текста на главной странице для подтверждения перехода на главную страницу')
    def get_text_on_recovery_button(self):
        return self.get_text_by_element(LoginPageLocator.RECOVERY_PASSWORD_BLOCK)

    def check_recovery_password(self):
        self.go_to_recovery_page()
        self.click_on_element(LoginPageLocator.PASSWORD_RECOVERY_FIELD)
        self.set_text_to_element(LoginPageLocator.PASSWORD_RECOVERY_FIELD, TestUserData.user_email)
        self.click_on_element(LoginPageLocator.PASSWORD_RECOVERY_BUTTON)
    def get_text_recovery_field(self):
        return self.get_text_by_element(LoginPageLocator.CODE_FROM_EMAIL)

    def check_focus_eye_button(self):
        time.sleep(3)
        self.click_on_element(LoginPageLocator.EYE_BUTTON)
        time.sleep(3)
        return self.wait_and_find_element(LoginPageLocator.NEW_PASSWORD_FIELD).get_attribute('class')
