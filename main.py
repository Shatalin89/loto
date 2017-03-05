from card import Card
from gamer import Gamer
from Game import Game
import os
import time
card1 = Card().get_card()
card2 = Card().get_card()
gamer1 = Gamer('hum', 'Player1', card1)
gamer2 = Gamer('pc', 'Computer', card2)
game = Game(gamer1, gamer2)
i=0


while not game.flag_end:
    os.system('clear')
    print('Ход - {}, выпавшие номера: {}'.format(game.get_num_move(), game.get_move_list()))
 #   print(game.get_card_in_gamer1())
  #  print(game.get_card_in_gamer2())
    num = game.gen_num()
    coor2 = game.gamer2.check_num(num)
#    coor2 = game.gamer2.check_num(num)

    
    if game.gamer2.type == 'pc' and coor2 != []:
         game.gamer2.remove_num(coor2)
         print('Удалил {}'.format(num))
    print(game.get_card_in_gamer2())

    i += 1
    time.sleep(2)
    if i == 50:
        break
