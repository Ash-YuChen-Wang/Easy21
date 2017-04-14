import Agent
import State
import random
import numpy as np


class Monte_Carlo_Control(object):
    def __init__(self):
        self.N = np.zeros([21, 10, 2])  # player score 1-21 | dealer first card 1-10 | HIT or STICK
        self.Q = np.zeros([21, 10, 2])

    def update(self, game):
        game_return = sum(game.rewards)
        counter = 0
        for state in game.states:
            self.N[state.player_score-1, state.dealer_score-1, game.actions[counter]] += 1
            self.Q[state.player_score-1, state.dealer_score-1, game.actions[counter]] += \
                1 / self.N[state.player_score-1, state.dealer_score-1, game.actions[counter]] * (
                    game_return - self.Q[state.player_score-1, state.dealer_score-1, game.actions[counter]])
            counter += 1


class Policy(object):
    def __init__(self):
        pass

    def action(self, state, k,Q):
        pass


class Epsilon_Greedy(Policy):
    n0 = 100
    def action(self, state, k, MC):
        epsilon = self.n0/(self.n0+MC.N[state.player_score-1, state.dealer_score-1,Agent.HIT]+MC.N[state.player_score-1, state.dealer_score-1,Agent.STICK])
        rand = random.random()
        if rand <= epsilon:  # then choose action randomly
            return random.choice([Agent.STICK, Agent.HIT])
        else:  # or choose greedy action
            if MC.Q[state.player_score-1, state.dealer_score-1, Agent.HIT] >= MC.Q[state.player_score-1, state.dealer_score-1, Agent.STICK]:
                return Agent.HIT
            else:
                return Agent.STICK