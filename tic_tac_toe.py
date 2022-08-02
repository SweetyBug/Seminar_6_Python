import random


def pr(tb):
    for i in tb:
        print(i)
    print('-----------------')


def user_go(tb):
    x, y = map(int, input('Введите индекс ряда и индекс столбца: ').split())
    if tb[x][y] == '*':
        tb[x][y] = 'x'
    else:
        print('Эта ячейка занята, введите другие значение!')
        user_go(tb)


def bot_go(tb):
    x = random.randint(-1, 2)
    y = random.randint(-1, 2)
    if tb[x][y] == '*':
        tb[x][y] = '0'
    else:
        bot_go(tb)


def game(ug, bg, tb, p):
    if (tb[0][0] == tb[0][1] == tb[0][2]) and ('*' not in tb[0]):
        p(tb)
        if tb[0][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[1][0] == tb[1][1] == tb[1][2]) and ('*' not in tb[1]):
        p(tb)
        if tb[1][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[2][0] == tb[2][1] == tb[2][2]) and ('*' not in tb[2]):
        p(tb)
        if tb[2][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[0][0] == tb[1][0] == tb[2][0]) and (tb[1][0] != '*'):
        p(tb)
        if tb[0][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[0][1] == tb[1][1] == tb[2][1]) and ('*' not in tb[1]):
        p(tb)
        if tb[0][1] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[0][2] == tb[1][2] == tb[2][2]) and ('*' not in tb[1]):
        p(tb)
        if tb[0][2] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[0][0] == tb[1][1] == tb[2][2]) and ('*' not in tb[1]):
        p(tb)
        if tb[0][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    elif (tb[2][0] == tb[1][1] == tb[0][2]) and ('*' not in tb[1]):
        p(tb)
        if tb[2][0] == 'x':
            print("Поздравляю, вы победили!")
        else:
            print('Упс... Кажется вы проиграли.')
    else:
        ug(tb)
        if '*' in tb[0] or '*' in tb[1] or '*' in tb[2]:
            bg(tb)
            p(tb)
            game(ug, bg, tb, p)
        else:
            p(tb)
            print('Ничья!')


table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

game(user_go, bot_go, table, pr)
