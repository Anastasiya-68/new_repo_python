# Тест 1. Ожидание динамической загрузки данных
# Шаги

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Открыть страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найти и нажать на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "div[id='start'] button")
    start_btn.click()

    # 3. Дождаться появления текста "Hello World!"
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div[id='finish'] h4"), "Hello World!"
        )
    )

    # 4. Сделать скриншот страницы
    driver.save_screenshot("screenshots/screen_Hello_World.png")

    # 5. Проверить, что появившийся текст равен "Hello World!"
    message = driver.find_element(By.CSS_SELECTOR, "div[id='finish'] h4")
    assert message.text == "Hello World!"
    "Сообщение 'Hello World!' не появилось"

    driver.quit()
