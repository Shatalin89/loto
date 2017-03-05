from  random import  randint

class Game:

    def __init__(self, gamer1, gamer2):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.list_num = []
        self.num_move = 0
        self.flag_end = False

    def gen_num(self):
        flag_move = False
        while not flag_move:
            num = randint(1, 90)
            if num not in self.list_num:
                self.list_num.append(num)
                self.num_move += 1
                flag_move = True
        return num

    def get_card_in_gamer1(self):
        return self.gamer1.get_my_card()

    def get_card_in_gamer2(self):
        return self.gamer2.get_my_card()

    def get_num_move(self):
        return self.list_num


    def check_winner(self):
        pass

    def start_game(self):
        pass