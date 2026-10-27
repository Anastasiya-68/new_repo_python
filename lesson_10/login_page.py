from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу авторизации.

        :param driver: Экземпляр WebDriver для управления браузером.
        :return: Ничего не возвращает (None).
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self) -> None:
        """
        Открывает главную страницу авторизации интернет-магазина в браузере.

        :return: Ничего не возвращает (None).
        """
        self.driver.get(
            "https://www.saucedemo.com/"
        )

    def authorization(self) -> None:
        """
        Находит поля для ввода учётных данных и заполняет их
        стандартным логином и паролем.

        Метод ожидает появления полей на странице перед тем, как ввести текст.

        :return: Ничего не возвращает (None).
        """
        user_name_input = self.wait.until(
            EC.presence_of_element_located(self.USER_NAME_INPUT)
        )
        user_name_input.send_keys("standard_user")

        password_input = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.send_keys("secret_sauce")

    def login_btn(self) -> None:
        """
        Дожидается появления кнопки входа (Login) и кликает по ней.

        :return: Ничего не возвращает (None).
        """
        login_btn = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BTN)
        )
        login_btn.click()
