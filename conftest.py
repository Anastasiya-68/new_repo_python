import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser") or "chrome"

    if browser == "chrome":
        chrome_options = Options()
        
        # 1. Подавляем проверку безопасности 
        chrome_options.add_argument("--disable-features=PasswordLeakDetection,PasswordProtection")
        chrome_options.add_argument("--safebrowsing-disable-leak-detection")
        
        # 2. Глубокий отладочный флаг, который отключает алерты утечки паролей при тестировании
        chrome_options.add_experimental_option("prefs", {
            "reduce-security-for-testing": True,  # Критический флаг для обхода алертов
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        
        driver = webdriver.Chrome(options=chrome_options)
        
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"Неподдерживаемый браузер: {browser}")

    yield driver
    driver.quit()
