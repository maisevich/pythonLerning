# 2. Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

list = []
n = int(input("Задайте количество чисел в списке: "))
for i in range(n):
	list.append(random.randint(-9,9))
print('Список:', list)

def mult_list(list):
    l = len(list) // 2 \
        if len(list) % 2 != 0 \
        else len(list) // 2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    print('Произведение пар чисел списка:', new_list)
mult_list(list)
