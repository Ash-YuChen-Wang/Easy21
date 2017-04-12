import Agent



class state(object)
    def __init__(self,player,dealer):
        self.player_score = player.score
        self.dealer_score = dealer.score

    def update(self,player,dealer):
        self.__init__(player,dealer)

    def print_state(self):
        print("Your score is ",self.player_score,"\nDealer's card is ",self.dealer_score)

    def is_terminal(self):

def step(state,action):
    state.print_state()

