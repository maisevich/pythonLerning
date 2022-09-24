#5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
#- 3
#- 6
#- 2
#- 1

#out
#5.099

expl = "Введите координаты двух точек на плоскости Х и Y"
print(expl)
x_A = float(input('X_A: '))
y_A = float(input('Y_A: '))
x_B = float(input('X_B: '))
y_B = float(input('Y_B: '))
from math import sqrt
print('Расстояние между точками:',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))