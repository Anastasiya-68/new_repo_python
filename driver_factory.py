from selenium import  webdriver

# сафари не поддерживает headless-режим.для него опции импортировать не надо

def create_driver(browser="chrome", headless=False):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    elif browser == "safari":
        if headless:
            raise ValueError("Опция не поддерживается")
        return webdriver.Safari()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        return  webdriver.Edge(options=options)
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
