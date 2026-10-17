# Тест 2. Работа с cookie
# Шаги

# Предварительные шаги
# Создано два аккаунта на https://gitflic.ru/.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Открыть страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # Установить cookie пользователя 1
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "MTlkZWM3NWEtMjNhZC00MzgxLTkwYWEtY2Y4MGE0ZjE3NWNi",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    # Обновить страницу
    driver.refresh()

    # Перейти на страницу пользователя 1
    driver.get("https://gitflic.ru/user/mstest2026")

    # Убедиться, что мы на странице пользователя 1
    user_1_name = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h6.mb-0"), "Анастасия Фролова"
        )
    )
    assert user_1_name, "Пользователь 'Анастасия Фролова' не отображается"

    # Получить и сохранить URL для user 1
    url_user_1 = driver.current_url

    # Разлогиниться (очистить куки)
    driver.delete_all_cookies()

    # Открыть главную страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # Установить cookie пользователя 2.
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "ZTRmZDEwN2QtNzBkMi00NTkyLWI2OTQtMmIzNDNmZjQ0MWUz",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    # Обновить страницу
    driver.refresh()

    # Перейти на страницу пользователя 2
    driver.get("https://gitflic.ru/user/anastasiya-kul1706")

    # Убедиться, что мы на странице пользователя 2
    user_2_name = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h6.mb-0"), "Анастасия Кулакова"
        )
    )
    assert user_2_name, "Пользователь 'Анастасия Кулакова' не отображается"

    # Получить и сохранить URL для user 2
    url_user_2 = driver.current_url

    # Проверить, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user_1 != url_user_2, (
        f"Ошибка: URL пользователей совпадают! ({url_user_1})"
    )

    driver.quit()
