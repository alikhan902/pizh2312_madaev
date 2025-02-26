from module import *
# Создание объектов римских чисел
num1 = Roman("X")   # 10
num2 = Roman("V")   # 5
num3 = Roman("III") # 3

# Вывод значений
print(num1)  # X
print(num2)  # V
print(num3)  # III

# Арифметические операции
sum_result = num1 + num2  # 10 + 5 = XV
sub_result = num1 - num3  # 10 - 3 = VII
mul_result = num2 * num3  # 5 * 3 = XV
div_result = num1 // num3 # 10 // 3 = III

# Вывод результатов
print(sum_result)  # XV
print(sub_result)  # VII
print(mul_result)  # XV
print(div_result)  # III

# Вызов объекта (__call__)
print(num1())  # 10 (получение числового значения)


# Преобразование в int
print(int(num1))  # 10
print(int(num2))  # 5