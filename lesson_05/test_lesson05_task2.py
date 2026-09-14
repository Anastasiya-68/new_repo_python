import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Шаги:


# 1. Открыть страницу https://httpbin.qa-territory.online/forms/post
def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    time.sleep(2)

    # 2. Найти поле ввода Customer name и убедиться, что оно активно для ввода
    input_field = driver.find_element(By.NAME, "custname")
    assert input_field.is_enabled()

    # 3. Ввести в поле Customer name имя Анастасия
    input_field.send_keys("Анастасия")

    # 4. Найти кнопку Submit order и нажать на нее
    submit_button = driver.find_element(
        By.XPATH, "//button[normalize-space()='Submit order']"
    )
    submit_button.click()

    # 5. Проверить, что после нажатия URL изменился
    assert "https://httpbin.qa-territory.online/post" in driver.current_url
    time.sleep(2)

    driver.quit()
