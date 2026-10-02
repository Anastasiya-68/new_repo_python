from pages.calc_page import CalcPage


def test_open_calculator(driver):
    calculator = CalcPage(driver)
    calculator.open_calc()
    calculator.delay_input()
    calculator.сalculator_buttons()
    final_result = calculator.get_result_addition()

    assert final_result == "15", (
        "Результат 15 не отобразился на экране калькулятора"
    )
