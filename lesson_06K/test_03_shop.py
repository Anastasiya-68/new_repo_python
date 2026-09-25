from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Шаги


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)

    # Открыть страницу https://www.saucedemo.com/ в браузере FireFox
    driver.get("https://www.saucedemo.com/")

    # Авторизоваться как пользователь standard_user
    user_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "user-name")
            )
            )
    user_name_input.send_keys("standard_user")

    password_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "password")
            )
            )
    password_input.send_keys("secret_sauce")

    login_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "login-button")
            )
            )
    login_btn.click()

    # Добавить в корзину товары:
    # Рюкзак Sauce Labs Backpack
    backpack_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")
            )
    )
    backpack_btn.click()

    # Футболка Sauce Labs Bolt T-Shirt
    t_shirt_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            )
    )
    t_shirt_btn.click()

    # Пижама Sauce Labs Onesie
    onesie_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-onesie")
            )
    )
    onesie_btn.click()

    # Перейти в корзину
    cart_btn = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "shopping_cart_link")
            )
    )
    cart_btn.click()

    # Нажать Checkout
    checkout_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "checkout")
            )
            )
    checkout_btn.click()

    # Заполнить форму данными: Анастасия Фролова 392000
    wait = WebDriverWait(driver, 3)

    first_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "first-name")
            )
            )
    first_name_input.clear()
    first_name_input.send_keys("Анастасия")

    last_name_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Last Name']")
        )
    )
    last_name_input.clear()
    last_name_input.send_keys("Фролова")

    zip_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "postal-code")
            )
            )
    zip_input.clear()
    zip_input.send_keys("392000")

    # Нажать кнопку Continue
    continue_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "continue")
            )
            )
    continue_btn.click()

    # Прочитать со страницы итоговую стоимость (Total)
    total_price = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
            )
    )
    text_total_price = total_price.text
    print(f"Текст стоимости с экрана: {text_total_price}")

    # Проверить, что итоговая сумма равна $58.29
    text_total_price = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "summary_total_label"), "$58.29"
        )
    )
    assert text_total_price, "Итоговая сумма не равна $58.29!"

    driver.quit()
