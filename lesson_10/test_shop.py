from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from order_page import OrderPage
from result_page import ResultPage
import allure


@allure.feature("Оформление заказа")
@allure.severity("critical")
@allure.title(
    "Успешное оформление заказа на покупку нескольких товаров в магазине"
)
@allure.description(
    "Тест проверяет полный цикл покупки: авторизацию,"
    " добавление трёх товаров в корзину, "
    "валидацию содержимого корзины, заполнение формы доставки"
    " и проверку итоговой стоимости."
)
def test_shop(driver) -> None:
    with allure.step("Открыть сайт магазина"):
        shop = LoginPage(driver)
        shop.open_page()

    with allure.step("Выполнить авторизацию под стандартным пользователем"):
        shop.authorization()

    with allure.step("Нажать кнопку входа 'Login'"):
        shop.login_btn()

    with allure.step("Добавить товары в корзину"):
        main_page = MainShopPage(driver)
        main_page.main_page()

    with allure.step("Перейти в корзину"):
        main_page.cart_page()

    with allure.step(
        "Проверить содержимое корзины на наличие добавленных товаров"
    ):
        cart = CartPage(driver)
        backpack, t_shirt, onesie = cart.product_list()

    assert backpack == "Sauce Labs Backpack", (
        "Рюкзак не найден в корзине"
    )
    assert t_shirt == "Sauce Labs Bolt T-Shirt", (
        "Футболка не найдена в корзине"
    )
    assert onesie == "Sauce Labs Onesie", (
        "Пижама не найдена в корзине"
    )

    with allure.step("Нажать на кнопку 'Checkout' для перехода к оформлению"):
        cart.checkout_btn()

    with allure.step("Заполнить форму персональными данными покупателя"):
        order = OrderPage(driver)
        order.data_form("Анастасия", "Фролова", "392000")

    with allure.step("Нажать кнопку 'Continue' для перехода к деталям заказа"):
        order.continue_btn()

    with allure.step("Проверить итоговую стоимость заказа (Total)"):
        result = ResultPage(driver)
        total_price = result.get_total_price()

        assert "$58.29" in total_price, (
            f"Итоговая сумма не равна $58.29."
            f"На странице отображается: {total_price}"
        )
