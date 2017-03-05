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

    def check_num(self, num):
        for i in range(3):
            for j in range(len(self.card[i])):
                if num == self.card[i][j]:
                    return [i,j]
                    break
        return []

    def remove_num(self, cord):
        if cord:
            self.card[int(cord[0])][int(cord[1])] ='--'
            return True
        else:
            return False