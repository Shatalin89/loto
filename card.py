from num_in_card import NumInCard
from random import randint


class Card:

    def generate_un_num(self, size, range):
        add_num = 0
        list_num = []
        while (add_num < size):
            num = randint(1, range)
            if num not in list_num:
                add_num += 1
                list_num.append(num)
        return list_num

    def create_blank_card(self):
        dx = 9
        dy = 3
        return [[' ' for x in range(dx)] for y in range(dy)]


    def fill_card(self):
        card = self.create_blank_card()
        list_num = self.generate_un_num(15, 98)
        newList = sorted(list_num[:5])+sorted(list_num[5:10])+sorted(list_num[10:15])
        iterList = iter(newList)
        for i in range(3):
            for j in sorted(self.generate_un_num(5, 8)):
                card[i][j] = next(iterList)
        return card

    def __init__(self):
        self.card_gamers = self.fill_card()

    def __str__(self):
        return self.card_gamers

    def check_num(self,num):
        for i in range(3):
            for j in self.card_gamers[i]:
                if num == j:
                    return [i,j]
                    break
        return []

    def remove_num(self, cord):
        self.card_gamers[int(cord[0])][int(cord[1])] = '-'


    def get_card(self):
        return self.card_gamers





card1 = Card()

print(card1.get_card())
print(card1.check_num(15))

