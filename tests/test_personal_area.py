import allure
import pytest
from pages.personal_area_page import PersonalAreaPage

class TestPersonalArea:

    @allure.title('Проверка перехода в "Личный кабинет"')
    @allure.description('Логинимся, кликаем по кнопке "Личный кабинет", \
                               проверяем наличие блока "Профиль" на странице')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_go_to_personal_area(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.go_to_personal_area_with_auth()
        assert personal_area_page.check_text_on_button_profile() == "Профиль"

    @allure.title('Проверка перехода в "История заказов"')
    @allure.description('Логинимся, кликаем по кнопке "Личный кабинет", \
              кликаем по кнопке "История заказов", проверяем что находимся в истории заказов')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_go_to_order_history(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.go_to_personal_area_with_auth()
        assert personal_area_page.check_history_orders() == 'История заказов'

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Логинимся, кликаем по кнопке "Личный кабинет", \
                  кликаем по кнопке "Выход", проверяем что находимся на странице авторизации')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_logout(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.go_to_personal_area_with_auth()
        assert personal_area_page.check_logout() == 'Войти'