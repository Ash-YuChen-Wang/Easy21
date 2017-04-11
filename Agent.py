import numpy as np
import Deck

# Return a card
def random_card(deck):
    num = np.random.randint(Deck.CARDS)
    return deck.deck[num]



class Agent(object):
    def __init__(self):
        self.holds = []

    def draw_black(self,deck):
        while True:
            card = random_card(deck)
            if card.color == Deck.BLACK:
                return self.holds.append(card)

class Player(Agent):
    pass

class Dealer(Agent):
    pass