from tic_tac_toe import *
from RLE import *
def user_menu():
    menu = '*** Крестики - нолики ***\n' \
           ' *** Задача №2 ***\n' \
           ' *** Сжать/восстановить данные ***\n' \
           ' Чтобы закончить введите "end"\n' \
           '------------------------------'
    user = input((f'Привет! Что будем проверять на этот раз?\n {menu} \n'))
    while user.lower() != 'end':
        if user.lower() == 'крестики - нолики' or user.lower() == 'крестики' or user.lower() == '1' or user.lower() == 'нолики':
            print('Твой противник - бот Серёжа :) \n Чтобы у тебя была фора, ты ходишь первый.')
            game(user_go, bot_go, table, pr)
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        elif user.lower() == 'задача №2' or user.lower() == 'задача 2' or user.lower() == '2':
            b = 1
        elif user.lower() == 'сжать/восстановить данные' or user.lower() == 'сжать данные' or user.lower() == '3' or user.lower() == 'восстановить данные':
            with open('RLE_input.txt', 'r') as ri, open('RLE_codding.txt', 'a', encoding='utf-8') as rc:
                a = True
                while a:
                    otvet = input('Вы хотите сжать данные или восстановить? \n')
                    if otvet.lower() == 'сжать':
                        us = ri.read()
                        code = rle_encod(us)
                        rc.write(f'\nЗакодированная информация:\n{code}')
                        a = False
                    elif otvet.lower() == 'восстановить':
                        us = ri.read()
                        decode = rle_decod(us)
                        rc.write(f'\nДекодированная информация:\n{decode}')
                        a = False
                    else:
                        print('Я тебя не понимаю. Давай ещё раз')
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        else:
            print('Я тебя не понимаю. Давай ещё раз')
            user = input((f'Что будем проверять?\n {menu} \n'))
