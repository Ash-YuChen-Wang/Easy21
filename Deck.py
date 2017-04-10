RANKS = 10
COLORS = 2
RED = 0
BLACK = 1
RED_PROB = 1 / 3
BLACK_PROB = 2 / 3


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

    def generate_new_deck(self):
        for color in range(COLORS):
            for rank in range(RANKS):
                card = Card(rank + 1, color)
                self.deck.append(card)
