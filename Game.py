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

    def move(self, gamer, num):
        coor = gamer.check_num(num)
        if gamer.type == 'pc':
            if coor !=[]:
                print('{} вычеркнул номер {}'.format(gamer.name, num))
                gamer.remove_num(coor)
        elif gamer.type == 'hum':
            question = input('{} вычеркнуть номер? {} y/n:'.format(gamer.name, num))
            if question == 'y' and coor != []:
                print('{} вычеркнул номер {}'.format(gamer.name, num))
                gamer.remove_num(coor)
            elif question == 'y' and coor == []:
                self.flag_end = True
                gamer.flag_loos = True
            elif question == 'n' and coor != []:
                self.flag_end = True
                gamer.flag_loos = True
            elif question == 'n' and coor == []:
                print()
                print('Действительно, нет номера {}'.format(num))
            else:
                print('чтото не пошло')
        else:
            print('чтото не пошло в принципе')

    def check_winner(self, gamer):
        if gamer.flag_loos == False and self.flag_end == False and gamer.check_card():
            #self.flag_end = True
            gamer.flag_win = True
            return True
        elif self.flag_end and gamer.flag_loos == False:
            gamer.flag_win = True
            return True
        elif self.flag_end and gamer.flag_loos == False and gamer.check_card() != True:
            gamer.flag_win = False
            return False
        elif gamer.check_card() != True and self.flag_end == True:
            gamer.flag_loos = True
            return False
        else:
            return False

    def get_card_in_gamer1(self):
        return self.gamer1.get_my_card()

    def get_card_in_gamer2(self):
        return self.gamer2.get_my_card()

    def get_move_list(self):
        return self.list_num

    def get_num_move(self):
        return self.num_move



