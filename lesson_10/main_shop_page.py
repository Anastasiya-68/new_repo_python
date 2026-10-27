from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    T_SHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver) -> None:
        """
        Инициализирует главную страницу магазина (каталог товаров).

        :param driver: Экземпляр WebDriver для управления браузером.
        :return: Ничего не возвращает (None).
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def main_page(self) -> None:
        """
        Находит кнопки добавления товаров и поочередно
        добавляет в корзину три товара.

        Метод последовательно ожидает появления кнопок для рюкзака, футболки
        и комбинезона, после чего кликает по каждой из них.

        :return: Ничего не возвращает (None).
        """
        backpack_btn = self.wait.until(
            EC.presence_of_element_located(self.BACKPACK_BTN)
        )
        backpack_btn.click()

        t_shirt_btn = self.wait.until(
            EC.presence_of_element_located(self.T_SHIRT_BTN)
        )
        t_shirt_btn.click()

        onesie_btn = self.wait.until(
            EC.presence_of_element_located(self.ONESIE_BTN)
        )
        onesie_btn.click()

    def cart_page(self) -> None:
        """
        Дожидается появления иконки/кнопки корзины и совершает по ней клик
        для перехода на страницу корзины.

        :return: Ничего не возвращает (None).
        """
        cart_btn = self.wait.until(
            EC.presence_of_element_located(self.CART_BTN)
        )
        cart_btn.click()
