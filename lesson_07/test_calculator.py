from pages.calc_page import CalcPage


def test_open_calculator(driver):
    calculator = CalcPage(driver)
    calculator.open_calc(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    calculator.delay_input("45")
    calculator.calculator_buttons()
    final_result = calculator.get_result_addition()

    assert final_result == "15", (
        "Результат 15 не отобразился на экране калькулятора"
    )
