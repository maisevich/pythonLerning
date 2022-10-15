#Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 3, 0, -1, 99, 333, -2]
#for i in a:
#    if i < 5:
#        print(i, end=', ')

#for elem in a:
#    if elem < 5:
#        print(elem)

#print(list(filter(lambda elem: elem < 5, a)))

#print([elem for elem in a if elem < 5])

#Задача 2
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#Нужно вернуть список, который состоит из
# элементов, общих для этих двух списков.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#print([elem for elem in a for elem in b if elem == 89])
#sult = [elem for elem in a if elem in b]
#print(sult)

#for i in a:
#    if i in b:
#        print(i, end=", ")

#colors =  ['red', 'green', 'blue']
#data = open('file.txt', 'a')
#data.writelines(colors)
#data.write('\nLINE 2\n')
#data.write('LINE 3\n')
#data.close()

#exit()
#path = 'file.txt'
#data = open(path, 'r')
#for line in data:
#    print(line)
#data.close()
#

#def f(x):
#    if x == 1:
#        return 'Integer'
#    elif x == 2.3:
#        return 23
#    else:
#        return

#import hello as h

#print(h.f(1))

#def new_string (symbol, count = 3):
#    return symbol * count

#print(new_string('&', 5))
#print(new_string('$'))
#print(new_string(4))

#def concentratio (*params):
#    res = 0
#    for item in params:
#        res += item
#    return res
#print(concentratio(1, 2, 3))


#рекурсия
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)