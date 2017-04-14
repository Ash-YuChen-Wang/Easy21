import random
import Deck
import RL

STICK = 0
HIT = 1

# Return a card
def random_card(deck):
    num = random.randint(0,Deck.CARDS-1)
    return deck.deck[num]



class Agent(object):
    def __init__(self,deck):
        self.holds = []
        self.deck = deck

    def put_in_holds(self,card):
        self.holds.append(card)

    def draw(self):
        """
        Randomly draw a card and put it in holds.
        
        :param deck: deck
        :return: None
        """
        self.put_in_holds(random_card(self.deck))

    @property
    def score(self):
        total_score = 0
        for card in self.holds:
            if card.color == Deck.BLACK:
                total_score += card.rank
            else:
                total_score -= card.rank
        return total_score

    def print_holds(self):
        for card in self.holds:
            card.print_card()


    def draw_black(self):
        while True:
            card = random_card(self.deck)
            if card.color == Deck.BLACK:
                return self.put_in_holds(card)


class Player(Agent):
    pass



class Dealer(Agent):
    pass