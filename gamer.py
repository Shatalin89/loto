class Gamer:

    def __init__(self, type, name, card):
        self.type = type
        self.name = name
        self.card = card

    def get_my_card(self):
        print('----- {:^16} -----'.format(self.name))
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                print(' {:^2}'.format(self.card[i][j]), end='')
            print()
        print('-' * 28)

