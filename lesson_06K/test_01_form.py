from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Шаги


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    # Открыть страницу в браузере Edge
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java"
        "/data-types.html")

    # Заполнить форму значениями:
    # Поле "First name"  Иван
    first_name_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']")
            )
    )
    first_name_input.clear()
    first_name_input.send_keys("Иван")

    # Поле "Last name"  Петров
    last_name_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='last-name']")
            )
    )
    last_name_input.clear()
    last_name_input.send_keys("Петров")

    # Поле "Address"  Ленина, 55-3
    address_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='address']")
            )
    )
    address_input.clear()
    address_input.send_keys("Ленина, 55-3")

    # Поле "E-mail"  test@skypro.com
    email_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='e-mail']")
            )
    )
    email_input.clear()
    email_input.send_keys("test@skypro.com")

    # Поле "Phone number"  +7985899998787
    phone_number_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='phone']")
            )
    )
    phone_number_input.clear()
    phone_number_input.send_keys("+7985899998787")

    # Поле "Zip code"  *оставить пустым
    zip_code_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='zip-code']")
            )
    )
    zip_code_input.clear()
    assert zip_code_input.get_attribute(
        "value") == "", "Поле Zip code не пустое!"

    # Поле "City" Москва
    city_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='city']")
            )
    )
    city_input.clear()
    city_input.send_keys("Москва")

    # Поле "Country"  Россия
    country_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='country']")
            )
    )
    country_input.clear()
    country_input.send_keys("Россия")

    # Поле "Job position"  QA
    job_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='job-position']")
            )
    )
    job_input.clear()
    job_input.send_keys("QA")

    # Поле "Company" SkyPro
    company_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='company']")
            )
    )
    company_input.clear()
    company_input.send_keys("SkyPro")

    # Нажать кнопку Submit при помощи JavaScript
    submit_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")
            )
    )
    driver.execute_script("arguments[0].click();", submit_button)

    # Проверить, что поле Zip code подсвечено красным цветом (ошибка)
    zip_code_input = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")
        )
        )
    zip_code_color = zip_code_input.get_attribute("class")
    assert "alert-danger" in zip_code_color, (
        "Ошибка! Поле Zip code не подсвечено красным."
    )

    # Проверить, что поле "First name" подсвечено зеленым цветом
    first_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "first-name")
            )
            )
    first_name_color = first_name_input.get_attribute("class")
    assert "alert-success" in first_name_color, (
        "Ошибка! Поле First name не подсвечено зеленым."
    )

    # Проверить, что поле "Last name name" подсвечено зеленым цветом
    last_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "last-name")
            )
            )
    last_name_color = last_name_input.get_attribute("class")
    assert "alert-success" in last_name_color, (
        "Ошибка! Поле Last name не подсвечено зеленым."
    )

    # Проверить, что поле "Address" подсвечено зеленым цветом
    address_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "address")
            )
            )
    address_input_color = address_input.get_attribute("class")
    assert "alert-success" in address_input_color, (
        "Ошибка! Поле Address не подсвечено зеленым."
    )

    # Проверить, что поле "E-mail" подсвечено зеленым цветом
    email_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "e-mail")
            )
            )
    email_input_color = email_input.get_attribute("class")
    assert "alert-success" in email_input_color, (
        "Ошибка! Поле E-mail не подсвечено зеленым."
    )

    # Проверить, что поле "Phone number" подсвечено зеленым цветом
    phone_number_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "phone")
            )
            )
    phone_number_color = phone_number_input.get_attribute("class")
    assert "alert-success" in phone_number_color, (
        "Ошибка! Поле Phone number не подсвечено зеленым."
    )

    # Проверить, что поле "City" подсвечено зеленым цветом
    city_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "city")
            )
            )
    city_input_color = city_input.get_attribute("class")
    assert "alert-success" in city_input_color, (
        "Ошибка! Поле City не подсвечено зеленым."
    )

    # Проверить, что поле "Country" подсвечено зеленым цветом
    country_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "country")
            )
            )
    country_input_color = country_input.get_attribute("class")
    assert "alert-success" in country_input_color, (
        "Ошибка! Поле Country не подсвечено зеленым."
    )

    # Проверить, что поле "Job position" подсвечено зеленым цветом
    job_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "job-position")
            )
            )
    job_input_color = job_input.get_attribute("class")
    assert "alert-success" in job_input_color, (
        "Ошибка! Поле Job position не подсвечено зеленым."
    )

    # Проверить, что поле "Company" подсвечено зеленым цветом
    company_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "company")
            )
            )
    company_input_color = company_input.get_attribute("class")
    assert "alert-success" in company_input_color, (
        "Ошибка! Поле Company не подсвечено зеленым."
    )

    driver.quit()
