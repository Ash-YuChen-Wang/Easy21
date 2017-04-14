import Agent
class Policy(object):
    """
    Given a state , return HIT or STICK
    """
    def __init__(self,state):
        self.state = state

    def generate_action(self):
        pass

    def update(self):
        pass

class Ask_user(Policy):

    def generate_action(self):
        decision = input('Press h to hit or s(or any other character) to stick :')
        if decision == 'h':  # No input validation here , maybe adding one could be necessary
            return Agent.HIT
        else:
            return Agent.STICK


class Until_17(Policy):

    def generate_action(self):
        if self.state.dealer_score < 17:
            return Agent.HIT
        else:
            return Agent.STICK