# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.

while True:
    n = int(input("Введите число N больше 20 для формирования диапазона: "))
    if n > 20:
        list = [i for i in range(20, n + 1) if i % 20 == 0 or i % 21 == 0]
        print(f"Список чисел кратных 20 или 21 в диапазоне [20...{n}]: ", list)
        break
    else:
        print("Вы ввели неверное число.")


