# 1. Вычислить число c заданной точностью d

import random

num = random.random()
print('Дано число: ', num)
dec = int(input(f'Задайте величину вычисления точности числа {num}: '))
print(round(num, dec))
