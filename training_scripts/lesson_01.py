# Задание 1.
# 1.1. Создайте переменную

my_height = 165
print(my_height)


# 1.2. Перезапишите переменную
my_name = "Anastasiya"
my_name = "Anastasiya Frolova"
print(my_name)


# 1.3. Получите пользовательский ввод 
pet_name = input("Как зовут вашего питомца?")
print("Ваш любимчик - " + pet_name)


# 1.4. Создание функции
def print_python():
    print("Учу Python!")
print_python()


# 1.5. Параметризация функций.
def print_letter(let):
    print(let, end="")


print_letter("С")
print_letter("т")
print_letter("у")
print_letter("д")
print_letter("е")
print_letter("н")
print_letter("т")