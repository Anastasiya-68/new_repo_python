import pytest
from selenium import webdriver
from lesson_08.project_page import ProjectApi

api = ProjectApi("https://ru.yougile.com")

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

# Фикстура для автоматического удаления проекта после теста
@pytest.fixture
def project_cleanup():
    context = {"id": None}
    
    yield context
    
    if context["id"]:
        api.delete_project(context["id"])
