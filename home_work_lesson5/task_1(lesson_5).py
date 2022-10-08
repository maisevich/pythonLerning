# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел..

import re

i = False
while not i:
    text = input("Введите текст со словами, содержащими 'абв' : \n")
    if re.findall(r'\d',text) == []:
        i = True
        print(text)
    else:
        print("Данные введены неверно, попробуйте еще раз.")

del_word = "абв"
lst = [i for i in text.split() if del_word not in i]

print(f'Результат: {" ".join(lst)}')
