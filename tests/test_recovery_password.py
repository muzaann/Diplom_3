import allure
import pytest
from pages.login_page import LoginPage


class TestRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Кликаем на кнопку "Личный кабинет", кликаем на кнопку "Восстановить пароль", \
                        проверяем переход на страницу восстановления пароля')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_open_recovery_page(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        login_page = LoginPage(driver)
        login_page.go_to_recovery_page()
        assert login_page.get_text_on_recovery_button() == 'Восстановить'

    @allure.title('Проверка ввода e-mail и клика по кнопке "Восстановить"')
    @allure.description('Переходим на страницу восстановления пароля, вводит e-mail, кликаем на кнопку \
                           "Восстановить", проверяем появление поля "Введите код из письма"')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_recovery_password(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        login_page = LoginPage(driver)
        login_page.check_recovery_password()
        assert login_page.get_text_recovery_field() == 'Введите код из письма'

    @allure.title('Проверка активности поля пароля при клике на показать/скрыть')
    @allure.description('Переходим на страницу восстановления пароля, вводит e-mail, кликаем на кнопку \
                               "Восстановить", кликаем на значек "глаза", проверяем, что поле стало активным')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_focused_password_field(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        login_page = LoginPage(driver)
        login_page.check_recovery_password()
        assert "input__placeholder-focused" in login_page.check_focus_eye_button()