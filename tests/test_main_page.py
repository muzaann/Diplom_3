import allure
import pytest
from pages.main_page import MainPage

class TestMainPage:

    @allure.title('Проверка перехода в "Конструктор"')
    @allure.description('Кликаем на кнопку "Лента заказов", \
                  кликаем по кнопке "Конструктор", проверяем что на странице есть блок "Соберите бургер"')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_go_to_assambler(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.go_to_assambler()
        assert main_page.check_assambler_text() == "Соберите бургер"

    @allure.title('Проверка перехода в "Конструктор"')
    @allure.description('Кликаем на кнопку "Лента заказов", \
                       проверяем что на странице есть блок "Лента заказов"')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_go_to_order_feed(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        assert main_page.check_order_feed_text() == "Лента заказов"

    @allure.title('Проверка появления высплывающего окна с деталями об ингредиенте"')
    @allure.description('Кликаем на ингредиент, \
                           проверяем появление высплывающего окна с текстом "Детали ингредиента"')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_get_ingredient_info(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.get_info_ingredient()
        assert main_page.check_text_about_ingredient() == "Детали ингредиента"

    @allure.title('Проверка закрытия высплывающего окна с деталями об ингредиенте"')
    @allure.description('Кликаем на ингредиент, нажимаем крестик на всплывающем окне\
                               проверяем что всплывающее окно закрылось')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_close_ingredient_info(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.get_info_ingredient()
        main_page.close_info_ingredient()
        assert 'opened' not in main_page.check_ingredient_info_closed()

    @allure.title('Проверка увеличения счетчика ингредиета при добавлении')
    @allure.description('Перетягиваем инредиент в корзину, проверяем что счетчки ингредиента \
                                   увеличивается')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_add_ingredients(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.add_bun_to_cart()
        assert main_page.check_ingredients_counter() == '2'

    @allure.title('Проверка оформления заказа залогиненым пользователем')
    @allure.description('Логинимся, добавляем ингредиенты в корзину, нажимаем кнопку \
                    "Оформить заказ", проверяем наличие во всплывающем окне идентификатора заказа')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_order(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        main_page = MainPage(driver)
        main_page.login()
        main_page.add_bun_to_cart()
        assert main_page.check_order() == 'идентификатор заказа'
