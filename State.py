import Agent



class State(object):
    def __init__(self,player,dealer):
        self.player_score = player.score
        self.dealer_score = dealer.score


    def next_state(self,player,dealer):
        """
        
        :param player: 
        :param dealer: 
        :return: A new State instance 
        """
        return State(player,dealer)

    def print_state(self):
        print("Your score is ",self.player_score,"\nDealer's card is ",self.dealer_score)

    def add_to_game(self,game):
        game.add_state(self)

    def player_terminal(self):
        if self.player_score > 21 or self.player_score < 1:
            return True
        else:
            return False

    def dealer_terminal(self):
        if self.dealer_score > 21 or self.dealer_score < 1:
            return True
        else:
            return False

class Game(object):
    def __init__(self):
        self.states = []
        self.reward = None

    def add_state(self,state):
        self.states.append(state)




def step(state,action):
    state.print_state()

