# Задача №11: Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input("Введите число: "))
lst = []
for i in range(number):
    lst.append((-3)**i)
print(f"Итоговая последовательность: {lst}")

# улучшение

lst = [(-3)**i for i in range(number)]
print(f"Итоговая последовательность после применения list comprehension: {lst}")

# Задача №12: Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число: "))
d = {i : 3*i + 1 for i in range(1,number+1)}
print(f"Итоговая последовательность: {d}")

# Задача №13: Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.


str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

# первый способ
print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")

# второй способ
count = 0
k = 1
for i in range(0,len(str1) - len(str2),k):
    if str2 in str1[i:i+len(str2)]:
        count += 1
        k = len(str2)
    else:
        k = 1
print(f"Вторая строка входит в первую {count} раз(а).")

# Задача №14: Подсчитать сумму цифр в вещественном числе.

number = float(input("Введите вещественное число: "))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Сумма цифр вещественного числа равна = {summ}")

# улучшение

new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр вещественного числа равна = {new_sum}")

# Задача №15: Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

N = int(input("Введите N для набора произведений чисел от 1 до N: "))
lst = [1]
for i in range(2, N+1):
    lst.append(lst[i-2] * i)
print(f"Итоговый набор {lst}")

# улучшение
lst = [ lst[i-2] * i if lst[i-2] != 0 else 1 for i in range(2, N+1) ]
print(f"Итоговый набор {lst}")

# Задача №17: Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs

# улучшение

n = int(input("Введите число N: "))
lst_number = [i for i in range(-n, n+1)]
write_file(n)
lst_index = read_file()
prod = 1
for i in range(len(lst_index)):
    prod *= lst_number[lst_index[i]]
print(f"Результат равен = {prod}")

# Задача №18: Реализовать алгоритм перемешивания списка.

import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")

# Задача №19: Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

from time import time
print(f'Случайное число от 0 до 99 = {int(time() % 1 * 100)}')

# x(n + 1) = (a * x (n) + b) % m
m = 100
b = 3
a = 2
x = 1
c = 50

list = []

for i in range (c):
    x = (a * x + b) % m
    list.append(x)

print(list)

# Задача №20: Определить, присутствует ли в заданном списке строк, некоторое число

lst_len = int(input("Введите количество строк для создания списка: "))
lst = [input(f"Введие {i+1} строку: ") for i in range(lst_len)]
number = input("Введите число для поиска: ")
flag = False
for i in lst:
    if number in i:
        flag = True
        break
print("Присутствует" if flag else "Не присутствует")