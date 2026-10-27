from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        :return: Ничего не возвращает (None).
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def data_form(
            self, first_name: str, last_name: str, zip_code: int | str
            ) -> None:
        """
        Очищает поля формы оформления заказа
        и заполняет их персональными данными покупателя.

        :param first_name: Строка с именем пользователя.
        :param last_name: Строка с фамилией пользователя.
        :param zip_code: Почтовый индекс
        (может быть передан как число int, так и строка str).
        :return: Ничего не возвращает (None).
        """
        first_name_input = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        zip_input = self.wait.until(
            EC.presence_of_element_located(self.ZIP_INPUT)
        )
        zip_input.clear()
        zip_input.send_keys(str(zip_code))

    def continue_btn(self) -> None:
        """
        Дожидается появления кнопки продолжения оформления
        (Continue) и кликает по ней.

        :return: Ничего не возвращает (None).
        """
        continue_btn = self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BTN)
        )
        continue_btn.click()
