# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.

import random

rand_list = []
n = int(input("Задайте количество чисел в списке: "))
for i in range(n):
	rand_list.append(random.randint(1,9))
print('Список:', rand_list)

new_list = [i for i in rand_list if rand_list.count(i) == 1]

print(f"Список неповторяющихся элементов: {new_list}")