from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver) -> None:
        """
        Инициализирует финальную страницу с результатами
        заказа (итоговым чеком).

        :param driver: Экземпляр WebDriver для управления браузером.
        :return: Ничего не возвращает (None).
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_total_price(self) -> str:
        """
        Дожидается видимости элемента с итоговой стоимостью
        и возвращает его текстовое содержимое.

        :return: Строка (str) с полным текстом итоговой стоимости.
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        )
        return total_element.text
