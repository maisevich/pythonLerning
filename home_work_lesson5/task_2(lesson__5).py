# 2. Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите данные для сжатия: '))
with open('text_words.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle_encode(my_text)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)