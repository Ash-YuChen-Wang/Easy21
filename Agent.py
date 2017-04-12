import numpy as np
import Deck

STICK = 0
HIT = 1

# Return a card
def random_card(deck):
    num = np.random.randint(Deck.CARDS)
    return deck.deck[num]



class Agent(object):
    def __init__(self):
        self.holds = []

    def put_in_holds(self,card):
        self.holds.append(card)

    def draw(self,deck):
        """
        Randomly draw a card and put it in holds.
        
        :param deck: deck
        :return: None
        """
        self.put_in_holds(random_card(deck))

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


    def draw_black(self,deck):
        while True:
            card = random_card(deck)
            if card.color == Deck.BLACK:
                return self.put_in_holds(card)

class Player(Agent):
    def user_decide(self):
        decision = input('Press h to hit or s(or any other character) to stick :')
        if decision == 'h': # No input validation here , maybe adding one could be necessary
            return HIT
        else:
            return STICK


    def user_turn(self,deck):
        while True:
            if self.user_decide() == HIT:
                self.draw(deck)
            else:
                break


class Dealer(Agent):
    def policy(self,deck):
        while self.score < 17:
            self.draw(deck)