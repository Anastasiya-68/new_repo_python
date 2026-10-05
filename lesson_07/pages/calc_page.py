from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY_INPUT_BUTTON = (By.ID, "delay")
    SEVEN_BUTTON = (By.XPATH, "//span[text()='7']")
    SUM_BUTTON = (By.XPATH, "//span[text()='+']")
    EIGHT_BUTTON = (By.XPATH, "//span[text()='8']")
    EQUAL_BUTTON = (By.XPATH, "//span[text()='=']")
    FIELD_RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Открыть страницу калькулятора в браузере Google Chrome
    def open_calc(self, url):
        self.driver.get(url)

    # В поле ввода задержки ввести значение 45
    def delay_input(self, delay_time):
        delay_input_button = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT_BUTTON)
        )
        delay_input_button.clear()
        delay_input_button.send_keys(str(delay_time))

    # Нажать на кнопки: "7", "+", "8" и "="
    def calculator_buttons(self):
        seven_btn = self.wait.until(
            EC.presence_of_element_located(self.SEVEN_BUTTON)
        )
        seven_btn.click()

        sum_btn = self.wait.until(
            EC.presence_of_element_located(self.SUM_BUTTON)
        )
        sum_btn.click()

        eight_btn = self.wait.until(
            EC.presence_of_element_located(self.EIGHT_BUTTON)
        )
        eight_btn.click()

        equal_btn = self.wait.until(
            EC.presence_of_element_located(self.EQUAL_BUTTON)
        )
        equal_btn.click()

    def get_result_addition(self):
        long_wait = WebDriverWait(self.driver, 48)
        long_wait.until(
            EC.text_to_be_present_in_element(self.FIELD_RESULT, "15")
        )
        return self.driver.find_element(*self.FIELD_RESULT).text
