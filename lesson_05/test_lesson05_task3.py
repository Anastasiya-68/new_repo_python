from selenium import webdriver
from selenium.webdriver.common.by import By

# Шаги
# 1. Открыть страницу https://httpbin.qa-territory.online/links/10.


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 2. Найти все ссылки на странице (тег <a>)
    num_links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверить, что количество ссылок равно 9
    assert len(num_links) == 9

    # 4. Проверить, что все ссылки отображаются на странице
    for link in num_links:
        assert link.is_displayed()

    # 5. Проверить, что текст первой ссылки содержит "1"
    first_link = num_links[0]
    assert "1" in first_link.text

    driver.quit()
