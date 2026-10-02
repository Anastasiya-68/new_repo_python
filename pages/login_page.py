from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Открыть страницу авторизации
    def open_page(self):
        self.driver.get(
            "https://www.saucedemo.com/"
        )

    # Авторизоваться (ввести логин и пароль)
    def authorization(self):
        user_name_input = self.wait.until(
            EC.presence_of_element_located(self.USER_NAME_INPUT)
        )
        user_name_input.send_keys("standard_user")

        password_input = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.send_keys("secret_sauce")

    # Нажать кнопку входа Login
    def login_btn(self):
        login_btn = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BTN)
        )
        login_btn.click()
