#Задача 2. Напишите программу,
#которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число N :"))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)


