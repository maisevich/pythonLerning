day = int(input('Введите цифру, соответсвующую дню недели : '))
if day > 7 or day < 1:
    print('Повторите, пожалуйста, ввод.')
elif day == 6 or day == 7:
    print("Это выходной.")
else:
    print("Это не выходной")