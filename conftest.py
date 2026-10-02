from email.policy import default
import pytest
from selenium import webdriver
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--run_browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, firefox, safari, edge"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без UI)"
    )

@pytest.fixture(scope="session")
def driver(request):
    # из-за конфликта с установленным у меня Playwright у меня команда для браузера записана как
    # --run_browser (тк как --brawser зареган для команды в Playwright)
    browser_name = request.config.getoption("--run_browser")
    headless_mode = request.config.getoption("--headless")
    driver = create_driver(browser_name, headless_mode)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    # У меня возникла проблема с гостевой кукой. Поэтому мой код отличается от кода лектора.
    # ОБЯЗАТЕЛЬНО: Удалить гостевую куку SESSION, которую сайт создал автоматически.
    driver.delete_all_cookies()

    # Добавить мою актуальную куку со всеми параметрами безопасности из DevTools
    driver.add_cookie({
        "name": "SESSION",
        "value": "N2Q1MDMzMGQtOWVkYi00NzkzLWE0YTYtNjkwOTIyNTE5NmE5",
        "domain": "gitflic.ru",
        "path": "/",
        "httpOnly": True,  # Соответствует галочке HttpOnly из моего DevTools
        "secure": True  # Соответствует галочке Secure из моего DevTools
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru",
        "path": "/"
    })

    driver.refresh()
    yield driver
    driver.quit()

