# Задача 1. Задайте натуральное число N. Напишите
# программу, которая составит список простых множителей числа N.

number_n = int(input('Введите число N: '))
print(number_n)

prime_factor_list = []

factor = 2
while number_n > 1:
    while number_n % factor == 0:
        prime_factor_list.append(factor)
        number_n //= factor
    factor += 1

print(f'Простые множители - {prime_factor_list}')