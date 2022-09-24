#4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).


num_quarter = int(input('Задайте номер четверти: '))
expl = "Диапазон возможных координат в этой четверти: "
if num_quarter == 1:
    print(expl,'x > 0; y > 0;')
elif num_quarter == 2:
    print(expl,'x < 0; y > 0;')
elif num_quarter == 3:
    print(expl,'x < 0; y < 0;')
elif num_quarter == 4:
    print(expl,'x > 0; y < 0;')
else:
    print('Введите, пожалуйста, цифру от 1 до 4.')

