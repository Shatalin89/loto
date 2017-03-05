from card import Card
from gamer import Gamer
from Game import Game

card1 = Card()
card2 = Card()
gamer1 = Gamer('hum', 'Player1', card1.get_card())
gamer2 = Gamer('pc', 'Computer', card2.get_card())

game = Game(gamer1, gamer2)
while not game.flag_end:
    print(game.get_num_move())
    print(game.get_card_in_gamer1())
    print(game.get_card_in_gamer2())
    game.gen_num()
    print(game.get_num_move())
    break