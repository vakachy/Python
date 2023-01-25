
import random

sweets = 80  # начальное количество конфет
sweets_min = 1 # можно взять такое минимальное количество конфет
sweets_max = 28 # можно взять такое максимальное количество конфет
alert = f'\nВозмите правильное количество конфет!\n{sweets_min} - минимум; \
{sweets_max} - максимум; но не более остатка (естественно).\n'
exclam = 'Вы выиграли, '
# --------------------------------------------------------------- #

# жеребьевка
def Randomize(players_list):
    return random.choice(players_list)

# --------------------------------------------------------------- #
# ход игрока


def Human_Moves(sweets, sweets_min, sweets_max, player_s_Name):
    offer = f'Сделайте ход, {player_s_Name}: '
    alert = f'\nВозмите правильное количество конфет!\n{sweets_min} - минимум; \
{sweets_max} - максимум; но не более остатка (естественно).\n'
    flag = False
    while (not flag):
        human = int(input(offer))
        if (human > sweets or human not in range(sweets_min, sweets_max + 1)):
            print(alert)
            flag = False
        else:
            flag = True
    sweets = sweets - human
    return (sweets, human)
# --------------------------------------------------------------- #
# ход Бота/Bot's move


def Bot_Moves(sweets, sweets_min, sweets_max, player_s_Name):
    bot = random.randint(sweets_min, sweets_max)
    if (bot > sweets):
        bot = random.randint(sweets_min, sweets)
    sweets = sweets - bot
    print(f'{player_s_Name} взял {bot} конфет(у, ы)')
    return sweets, bot
# --------------------------------------------------------------- #
# ход умного Бота/Smart Bot's move


def SmartBot_Moves(sweets, sweets_min, sweets_max, player_s_Name, count, human=0):

    if (count == 1):
        bot = sweets % (sweets_min + sweets_max)
    else:
        if (sweets >= sweets_max):
            bot = (sweets_max+sweets_min)-human
        else:
            bot = sweets
    sweets = sweets - bot
    print(f'{player_s_Name} взял {bot} конфет(у, ы)')
    return sweets, bot
# --------------------------------------------------------------- #
# смена игрока/change player


def Change_Player(players_list, player_s_Name):
    if (player_s_Name == players_list[0]):
        return players_list[1]
    else:
        return players_list[0]
# --------------------------------------------------------------- #
# проверка на выигрыш


def Check(sweets):
    if sweets <= 0:
        return True
# --------------------------------------------------------------- #


print(f"\nВ игре участвуют два игрока под номером 1 и 2,\n\
либо Игрок 1 и Бот, либо Игрок 1 и Умный Бот.\n\
Игроки по очереди берут конфеты.\n\
Автоматическая жеребьевка определит, кто ходит первым.\n\
Минимум можно взять {sweets_min} конфету, максимум -- {sweets_max} конфет(ы) за один ход.\n\
Выигрывает тот, кто забирает все конфеты последним.\n")
print(f'Начальное количество конфет: {sweets}\n')

flag = False
while (not flag):
    print('Выбор режима игры:\n\
        1 - игра "Игрок 1 против Игрока 2"\n\
        2 - игра "Игрок 1 против Бота"\n\
        3 - игра "Игрок 1 против Умного Бота"')
    mode=int(input('Сделайте выбор: '))
    if (mode == 1):
        players_list = ['Игрок 1', 'Игрок 2']
        player_s_Name = Randomize(players_list)
        print(f'{player_s_Name} ходит первым.')
        while (sweets >= 0):
            print(f'\nОсталось    {sweets}    конфет(а, ы)')
            sweets, human = Human_Moves(sweets, sweets_min, sweets_max, player_s_Name)
            if (Check(sweets)):
                print('\n' + ' '.join([exclam, player_s_Name,'!']))
                break   
            player_s_Name = Change_Player(players_list, player_s_Name)
            flag = True
    elif (mode == 2):
        players_list = ['Игрок 1', 'Bot']
        player_s_Name = Randomize(players_list)
        print(f'{player_s_Name} ходит первым.')
        while (sweets >= 0):
            print(f'\nОсталось    {sweets}    конфет(ы)')
            if (player_s_Name == players_list[0]):
                sweets, human = Human_Moves(sweets, sweets_min, sweets_max, player_s_Name)
            else:
                sweets, bot = Bot_Moves(
                        sweets, sweets_min, sweets_max, player_s_Name)
            if (Check(sweets)):
                print('\n' + ' '.join([exclam, player_s_Name, '!']))
                break
            player_s_Name = Change_Player(players_list, player_s_Name)
            flag = True
    elif (mode==3):
        players_list = ['Игрок 1', 'SmartBot']
        count = 1
        player_s_Name = Randomize(players_list)
        print(f'{player_s_Name} ходит первым.')
        while (sweets >= 0):
            print(f'\nОсталось    {sweets}    конфет(а,ы)')

            if (player_s_Name == players_list[0]):
                sweets, human = Human_Moves(
                    sweets, sweets_min, sweets_max, player_s_Name)
            else:
                if (count == 1):
                    sweets, bot = SmartBot_Moves(
                        sweets, sweets_min, sweets_max, player_s_Name, count)
                else:
                    sweets, bot = SmartBot_Moves(
                        sweets, sweets_min, sweets_max, player_s_Name, count, human)
            if (Check(sweets)):
                print('\n' + ' '.join([exclam, player_s_Name, '!']))
                break
            player_s_Name = Change_Player(players_list, player_s_Name)
            count += 1
        flag = True
