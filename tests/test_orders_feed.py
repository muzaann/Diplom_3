import allure
import pytest
from pages.orders_feed_page import OrdersFeedPage


class TestOrderFeed:

    @allure.title('Проверка открытия всплывающего окна с деталями о заказе')
    @allure.description('Переходим в ленту заказов, кликаем на заказ, проверяем \
                        открытие всплывающего окна с информацией о составе заказа')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_info_order(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.go_to_order_feed()
        assert order_feed_page.get_order_info() == 'Cостав'

    @allure.title('Проверка отображения заказа пользователя на странице "Лента заказов"')
    @allure.description('Логинимся, оформляем заказ, сохраняем номер заказа на всплыващем окне, проверяем \
                            наличие заказа с этим номером в Ленте заказов')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_orders_from_orders_history(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.login()
        order_feed_page.create_order(driver)
        assert order_feed_page.get_order_number() in order_feed_page.get_orders_numbers()

    @allure.title('Проверка увеличения счетчика заказов, выполненных за все время"')
    @allure.description('Логинимся, оформляем заказ, проверяем что счетчик заказов за все время \
                                увеличился на 1')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_counter_all_time(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.login()
        order_feed_page.go_to_order_feed()
        before = order_feed_page.get_count_all_time()
        order_feed_page.go_to_constructor()
        order_feed_page.create_order(driver)
        order_feed_page.go_to_orders_feed_from_order_info()
        after = order_feed_page.get_count_all_time()
        assert int(after) == int(before) + 1

    @allure.title('Проверка увеличения счетчика заказов, выполненных за сегодня"')
    @allure.description('Логинимся, оформляем заказ, проверяем что счетчик заказов за сегодня \
                                    увеличился на 1')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_counter_today(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.login()
        order_feed_page.go_to_order_feed()
        before = order_feed_page.get_count_today()
        order_feed_page.go_to_constructor()
        order_feed_page.create_order(driver)
        order_feed_page.go_to_orders_feed_from_order_info()
        after = order_feed_page.get_count_today()
        assert int(after) == int(before) + 1

    @allure.title('Проверка появления номера нового заказа в блоке "В работе"')
    @allure.description('Логинимся, оформляем заказ, сохраняем его номер с всплывающего окна, \
                     проверяем наличие этого номера в разделе "В работе"')
    @pytest.mark.parametrize('any_driver', ['driver_firefox', 'driver_chrome'])
    def test_order_number_in_work(self, request, any_driver):
        driver = request.getfixturevalue(any_driver)
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.login()
        order_feed_page.create_order(driver)
        assert order_feed_page.get_order_number() in order_feed_page.get_orders_in_work()
