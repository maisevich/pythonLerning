def creating ():
    file = 'personal.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия, Имя, Должность, Отделение, Личный номер;\n')