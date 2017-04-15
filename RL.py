import Agent
import random
import numpy as np
import math


class Monte_Carlo_Control(object):
    def __init__(self):
        self.N = np.zeros([21, 10, 2])  # player score 1-21 | dealer first card 1-10 | HIT or STICK
        self.Q = np.zeros([21, 10, 2])

    def update(self, game):
        game_return = sum(game.rewards)
        counter = 0
        for state in game.states:
            self.N[state.player_score - 1, state.dealer_score - 1, game.actions[counter]] += 1
            self.Q[state.player_score - 1, state.dealer_score - 1, game.actions[counter]] += \
                1 / self.N[state.player_score - 1, state.dealer_score - 1, game.actions[counter]] * (
                    game_return - self.Q[state.player_score - 1, state.dealer_score - 1, game.actions[counter]])
            counter += 1


class Sarsa_Lambda(object):
    def __init__(self, lamb, gamma):
        self.lamb = lamb
        self.gamma = gamma
        self.N = np.zeros([21, 10, 2])
        self.Q = np.zeros([21, 10, 2])
        self.eligibility_trace = np.zeros([21, 10, 2])

    def Q_S_A(self, state, action):
        return self.Q[state.player_score - 1, state.dealer_score - 1, action]

    def N_S_A(self, state, action):
        return self.N[state.player_score - 1, state.dealer_score - 1, action]

    def E_S_A(self, state, action):
        return self.eligibility_trace[state.player_score - 1, state.dealer_score - 1, action]

    def init_eligibility_trace(self):
        self.eligibility_trace = np.zeros([21, 10, 2])

    def add_trace_N(self, state, action):
        self.eligibility_trace[state.player_score - 1, state.dealer_score - 1, action] += 1
        self.N[state.player_score - 1, state.dealer_score - 1, action] += 1

    def update(self, delta):
        for player_score in range(1, 22):
            for dealer_score in range(1, 11):
                for action in [Agent.STICK, Agent.HIT]:
                    alpha = 1 / self.N[player_score - 1, dealer_score - 1, action]
                    if not math.isinf(alpha):
                        self.Q[player_score - 1, dealer_score - 1, action] += alpha * delta * self.eligibility_trace[
                            player_score - 1, dealer_score - 1, action]
                        self.eligibility_trace[player_score - 1, dealer_score - 1, action] *= self.gamma * self.lamb
                    else:
                        pass


class Policy(object):
    def __init__(self):
        pass

    def action(self, state, k, Q):
        pass


class Epsilon_Greedy(Policy):
    n0 = 100

    def action(self, state, k, control):
        epsilon = self.n0 / (self.n0 + control.N[state.player_score - 1, state.dealer_score - 1, Agent.HIT] + control.N[
            state.player_score - 1, state.dealer_score - 1, Agent.STICK])
        rand = random.random()
        if rand <= epsilon:  # then choose action randomly
            return random.choice([Agent.STICK, Agent.HIT])
        else:  # or choose greedy action
            if control.Q[state.player_score - 1, state.dealer_score - 1, Agent.HIT] >= control.Q[
                        state.player_score - 1, state.dealer_score - 1, Agent.STICK]:
                return Agent.HIT
            else:
                return Agent.STICK
