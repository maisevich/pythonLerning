#Задача 5.** Реализуйте алгоритм перемешивания списка.
#Без функции shuffle из модуля random.

import random
ls = ['Hello', 'World', 'Rap', 1, 2, 8]
print(str(ls))
for i in range(len(ls) - 1, 0, -1):
    j = random.randint(0, i + 1)
    ls[i], ls[j] = ls[j], ls[i]
print(str(ls))
