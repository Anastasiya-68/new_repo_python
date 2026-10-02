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
        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_PRICE, "$58.29")
        )
        return self.driver.find_element(*self.TOTAL_PRICE).text
