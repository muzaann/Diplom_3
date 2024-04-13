import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator
from data import TestUserData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step ('Переход на страницу восстановления пароля')
    def go_to_recovery_page(self):
        self.click_on_element(LoginPageLocator.PERSONAL_AREA_BUTTON)
        self.click_on_element(LoginPageLocator.RECOVERY_PASSWORD_BUTTON)

    @allure.step ('Получение текста на кнопке восстановления пароля')
    def get_text_on_recovery_button(self):
        return self.get_text_by_element(LoginPageLocator.RECOVERY_PASSWORD_BLOCK)

    @allure.step('Ввод e-mail и клик по кнопке "Восстановить"')
    def check_recovery_password(self):
        self.go_to_recovery_page()
        self.click_on_element(LoginPageLocator.PASSWORD_RECOVERY_FIELD)
        self.set_text_to_element(LoginPageLocator.PASSWORD_RECOVERY_FIELD, TestUserData.user_email)
        self.click_on_element(LoginPageLocator.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Получение текста из поля "введите код из письма"')
    def get_text_recovery_field(self):
        return self.get_text_by_element(LoginPageLocator.CODE_FROM_EMAIL)

    @allure.step('Получения атрибута для проверки активности поля "пароль"')
    def check_focus_eye_button(self):
        self.click_on_element(LoginPageLocator.EYE_BUTTON)
        return self.get_attribute(LoginPageLocator.NEW_PASSWORD_FIELD, 'class')

