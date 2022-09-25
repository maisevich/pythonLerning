#Задача 4*. Напишите программу, которая принимает на вход 2 числа.
#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).

from random import randint
numbers = []
for i in range(8):
    numbers.append(randint (-30,30))
print(numbers)
def ls(numbers):
    count =0
    for element in numbers:
        count +=1
    return count
print('Всего элементов в списке: ', ls(numbers))
x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))
for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(mult)
