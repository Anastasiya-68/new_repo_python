from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Получить со страницы итоговую стоимость (Total)
    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        )
        return total_element.text
