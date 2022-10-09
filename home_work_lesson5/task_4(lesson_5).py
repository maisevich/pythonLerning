from random import *

welcome_text = ('Начало игры!')
print(welcome_text)

message = ['Сейчас играет ', 'Ход выполняет', ' Ставку делает']

def player_vs_player():
    candies_total = 2022
    max_take = 28
    count = 0
    player_1 = input('Введите имя игрока 1: ')
    player_2 = input('Введите имя игрока 2: ')

    print(f'\nИгра для {player_1} и  {player_2} начинается\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'{lucky} ходит первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {lucky}.'))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОстаток: {candies_total}')
            count = 1
        else:
            print('Конфеты закончились')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nПопробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОстаток {candies_total}')
            count = 0
        else:
            print('Конфеты закончились')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')

player_vs_player()
