from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    PRODUCT_BACKPACK = (
        By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name"
        )
    PRODUCT_T_SHIRT = (
        By.CSS_SELECTOR, "#item_1_title_link .inventory_item_name"
        )
    PRODUCT_ONESIE = (
        By.CSS_SELECTOR, "#item_2_title_link .inventory_item_name"
        )
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        :return: Ничего не возвращает (None).
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def product_list(self) -> tuple[str, str, str]:
        """
        Ожидает появления товаров в корзине и собирает их текстовые названия.

        Метод дожидается, пока в соответствующих элементах появится ожидаемый
        текст для рюкзака, футболки и комбинезона,
        после чего извлекает его.

        :return: Кортеж (tuple), содержащий три строки (str)
        с названиями товаров.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_BACKPACK, "Sauce Labs Backpack"
                )
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_T_SHIRT, "Sauce Labs Bolt T-Shirt"
                )
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_ONESIE, "Sauce Labs Onesie"
                )
        )

        backpack_text = self.driver.find_element(*self.PRODUCT_BACKPACK).text
        t_shirt_text = self.driver.find_element(*self.PRODUCT_T_SHIRT).text
        onesie_text = self.driver.find_element(*self.PRODUCT_ONESIE).text

        return backpack_text, t_shirt_text, onesie_text

    def checkout_btn(self) -> None:
        """
        Дожидается кликабельности и нажимает на кнопку перехода
        к оформлению заказа (Checkout).

        :return: Ничего не возвращает (None).
        """
        checkout_btn = self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BTN)
        )
        checkout_btn.click()
