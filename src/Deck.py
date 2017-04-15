CARDS = 30
RANGE = 10
RED = 0
BLACK = 1
RED_PROB = 1 / 3
BLACK_PROB = 2 / 3
RED_NUM = int(CARDS * RED_PROB)
BLACK_NUM = int(CARDS * BLACK_PROB)

NUMS = {RED: RED_NUM, BLACK: BLACK_NUM}


class Card(object):
    def __init__(self, rank, color):
        self.rank = rank
        # will be using 0 to represent red , 1 black
        self.color = color

    def print_card(self):
        print(self.rank, '  ', 'Red' if self.color == RED else 'Black')


class Deck:
    def __init__(self):
        self.deck = []
        self.generate_new_deck()


    def put_in_deck(self, card):
        self.deck.append(card)

    def generate_new_deck(self):
        for color, num in NUMS.items():
            for i in range(int(num / 10)):
                for rank in range(RANGE):
                    card = Card(rank + 1, color)
                    self.put_in_deck(card)

    def print_deck(self):
        for card in self.deck:
            card.print_card()
