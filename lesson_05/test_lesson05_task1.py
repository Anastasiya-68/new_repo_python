import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Шаги
# 1. Открыть страницу https://httpbin.qa-territory.online
def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    time.sleep(3)

    # 2. Найти и кликнуть на ссылку HTML Form
    link_name = driver.find_element(By.CSS_SELECTOR, "a[href='/forms/post']")
    link_name.click()
    time.sleep(2)

    # 3. Проверить, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # 4. Вернуться назад на главную страницу
    driver.back()
    time.sleep(2)

    # 5. Проверить, что вернулись на исходный URL
    link_by_text = driver.find_element(By.LINK_TEXT, "HTML Form")
    assert link_by_text.is_displayed()

    driver.quit()
