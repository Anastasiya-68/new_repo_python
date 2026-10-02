from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Заполнить форму данными: Анастасия Фролова 392000
    def data_form(self):
        first_name_input = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.clear()
        first_name_input.send_keys("Анастасия")

        last_name_input = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_input.clear()
        last_name_input.send_keys("Фролова")

        zip_input = self.wait.until(
            EC.presence_of_element_located(self.ZIP_INPUT)
        )
        zip_input.clear()
        zip_input.send_keys("392000")

    # Нажать кнопку Continue
    def continue_btn(self):
        continue_btn = self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BTN)
        )
        continue_btn.click()
