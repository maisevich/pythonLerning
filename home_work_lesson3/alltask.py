# HOME WORK


# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#def sum_index(list):
#    s = 0
#    for i in range(len(list)):
#        if i % 2 != 0:
#            s += list[i]
#    print(f"Сумма = {s}")
#list = [2, 3, 5, 9, 3]
#sum_index(list)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_list(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    print(new_list)

list = [2, 3, 4, 5, 6]
print(list)
mult_list(list)


# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

#lst = list(map(float, input("Введите числа через пробел:\n").split()))
#new_lst = [round(i%1,2) for i in lst if i%1 != 0]
#print(max(new_lst) - min(new_lst))

#Напишите программу, которая будет преобразовывать
# десятичное число в двоичное. Пример:

#s = ""
#n = int(input("Введите число:\n"))
#while n != 0:
#    s = str(n%2) + s
#    n //=2
#print(s)






