# 3. Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

n = int(input('Введите число: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)