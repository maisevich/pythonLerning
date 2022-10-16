from User_interface import get_info as gi

info = gi()
def writing_scv ():
    file = 'personal.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]} {info[1]}, {info[2]}, {info[3]}, {info[4]}\n\n\n')

def writing_txt ():
    file = 'personal.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]} {info[1]}\n{info[2]} {info[3]}\n{info[4]}\n\n\n')