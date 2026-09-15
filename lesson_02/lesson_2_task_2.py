def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Вызов функции и сохранение результата в переменную
test_year = 2000
result = is_year_leap(test_year)

# Вывод в консоль в нужном формате
print(f"год {test_year}: {result}")
