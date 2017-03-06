from card import Card
from gamer import Gamer
from Game import Game
import os
import time

def create_player():
    print('Выберите тип игрока')
    print('1 - Человек')
    print('2 - Компьютер')
    type = input('Введите номер:')
    while type not in ['1', '2']:
        type = input('Введите номер:')
    if type == '1':
        type = 'hum'
        name = input('Введите имя игрока:') or 'Player1'
    elif type == '2':
        type = 'pc'
        name = input('Введите имя игрока:') or 'Computer'
    card = Card().get_card()
    return Gamer(type, name, card)



gamer1 = create_player()
gamer2 = create_player()
game = Game(gamer1, gamer2)



while not game.flag_end:
    try:
        os.system('clear') #для очистки консоли в линуксе
    except:
        os.sysconf('cls') #для очистка консоли в винде

    num = game.gen_num()
    print('Ход - {}, выпавшие номера: {}'.format(game.get_num_move(), game.get_move_list()))
    game.get_card_in_gamer1()
    game.get_card_in_gamer2()
    game.move(gamer1, num)
    game.move(gamer2, num)
    if game.check_winner(gamer1) and game.check_winner(gamer2):
        print()
        print('Ничья!!!')
        game.flag_end = True
    elif game.check_winner(gamer1) :
        print()
        print('Победил {}'.format(gamer1.name))
        game.flag_end = True
    elif game.check_winner(gamer2):
        print()
        print('Победил {}'.format(gamer2.name))
        game.flag_end = True
    if game.flag_end:
        print()
        print('Конец игры')

    time.sleep(1)

