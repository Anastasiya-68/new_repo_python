from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Шаги


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)

    # Открыть страницу в браузере Google Chrome
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java"
        "/slow-calculator.html"
        )

    # В поле ввода задержки ввести значение 45
    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать на кнопку 7
    seven_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='7']"))
    )
    seven_btn.click()

    # Нажать на кнопку +
    sum_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='+']"))
    )
    sum_btn.click()

    # Нажать на кнопку 8
    eight_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='8']"))
    )
    eight_btn.click()

    # Нажать на кнопку =
    equal_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='=']"))
    )
    equal_btn.click()

    # Добавить ожидание 45 сек для выполнения задачи
    long_wait = WebDriverWait(driver, 48)

    # Проверить, что в окне отобразился результат 15 через 45 секунд
    result_found = long_wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result_found, "Результат 15 не отобразился на экране калькулятора!"

    driver.quit()
