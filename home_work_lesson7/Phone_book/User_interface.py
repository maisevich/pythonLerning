def get_info ():
    info = []
    last_name = input('Фамилия: ')
    info.append(last_name)
    first_name = input('Имя: ')
    info.append(first_name)
    job_title = input('Должность: ')
    info.append(job_title)
    departement = input('Отделение: ')
    info.append(departement)
    id = ''
    valid = False
    while not valid:
        try:
            id = input('Личный номер работника (из трех цифр): ')
            if len(id) != 3:
                print(id)
            else:
                id = int(id)
                valid = True
        except:
            print('ID должен состоять из цифр.')
    info.append(id)
    return info