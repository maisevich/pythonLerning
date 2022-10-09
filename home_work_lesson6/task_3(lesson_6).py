# 3.Написать функцию, элементы - имена сотрудников, возвращает словарь,
# ключи — первые буквы имен, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def lst (*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

print(lst("Кристина", "Саша", "Иван", "Анастасия", "Мария", "Jose"))