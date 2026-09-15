import pytest
from selenium import webdriver

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Выберите браузер chrome или firefox",
#     )


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"Неподдерживаемый браузер: {browser}")

    yield driver
    driver.quit()
