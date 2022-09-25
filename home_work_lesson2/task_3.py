# Задача 3. Задайте список из n чисел, заполненный по формуле (1+1/n)**n
# и выведите на экран их сумму.

n = int(input('Введите число N: '))
def ls(n):
    return [round((1 + 1 / n) ** n) for n in range(1, n + 1)]
print(ls(n))
print(round(sum(ls(n))))
