from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from pages.result_page import ResultPage


def test_shop(driver):
    # Открыть сайта магазина
    shop = LoginPage(driver)
    shop.open_page()

    # Авторизоваться
    shop.authorization()

    # Нажать кнопку входа Login
    shop.login_btn()

    # Добавить в корзину товары
    main_page = MainShopPage(driver)
    main_page.main_page()

    # Перейти в корзину
    main_page.cart_page()

    # Проверить содержимое корзины
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

    # Нажать на кнопку Checkout
    cart.checkout_btn()

    # Заполнить форму данными: Анастасия Фролова 392000
    order = OrderPage(driver)
    order.data_form()

    # Нажать кнопку Continue
    order.continue_btn()

    # Получить со страницы итоговую стоимость (Total)
    result = ResultPage(driver)
    total_price = result.get_total_price()

    assert "$58.29" in total_price, (
        f"Итоговая сумма не равна $58.29 : {total_price}"
    )
