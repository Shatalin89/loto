from random import randint


class Card:
    @staticmethod
    def generate_un_num(size, range_list):
        add_num = 0
        list_num = []
        while add_num < size:
            num = randint(1, range_list)
            if num not in list_num:
                add_num += 1
                list_num.append(num)
        return list_num

    @staticmethod
    def create_blank_card():
        return [[' ' for x in range(9)] for y in range(3)]

    def fill_card(self):
        card = self.create_blank_card()
        list_num = self.generate_un_num(15, 90)
        new_list = sorted(list_num[:5])+sorted(list_num[5:10])+sorted(list_num[10:15])
        iter_list = iter(new_list)
        for i in range(3):
            for j in sorted(self.generate_un_num(5, 8)):
                card[i][j] = next(iter_list)
        return card

    def __init__(self):
        self.card_gamers = self.fill_card()
        self.remove_num_list = []

    def check_num(self,num):
        for i in range(3):
            for j in range(len(self.card_gamers)):
                if num == self.card_gamers[i][j]:
                    return [i,j]
                    break
        return []

    def remove_num(self, cord):
        if cord:
            self.card_gamers[int(cord[0])][int(cord[1])] = '-'
            return True
        else:
            return False

    def get_card(self):
        return self.card_gamers



