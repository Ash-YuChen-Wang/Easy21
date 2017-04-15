from src import Agent, Deck, RL, State


def sarsa_lambda_control(episodes, lamb):
    EPISODES = episodes

    deck = Deck.Deck()

    sarsa = RL.Sarsa_Lambda(lamb, 1)
    policy = RL.Epsilon_Greedy()

    for k in range(EPISODES):
        terminated = False

        player = Agent.Player(deck)
        dealer = Agent.Dealer(deck)

        sarsa.init_eligibility_trace()

        player.draw_black()
        dealer.draw_black()

        state = State.State(player, dealer)
        # state.print_state()

        action = policy.action(state, k + 1, sarsa)

        while action == Agent.HIT:
            player.draw()
            sarsa.add_trace_N(state, Agent.HIT)
            if player.score > 21 or player.score < 1:  # Lose
                reward = -1
                delta = reward + 0 - sarsa.Q_S_A(state, Agent.HIT)
                sarsa.update(delta)
                terminated = True
                # print("Player BUST Lose !")
                break
            state_next = state.next_state(player, dealer)
            action_next = policy.action(state_next, k + 1, sarsa)
            delta = 0 + sarsa.gamma * sarsa.Q_S_A(state_next, action_next) - sarsa.Q_S_A(state, Agent.HIT)
            sarsa.update(delta)
            state = state_next
            action = action_next

        if not terminated:
            sarsa.add_trace_N(state, Agent.STICK)
            while dealer.score < 17:
                dealer.draw()
                if dealer.score > 21 or dealer.score < 1:  # Win
                    reward = 1
                    delta = reward + 0 - sarsa.Q_S_A(state, Agent.STICK)
                    sarsa.update(delta)
                    terminated = True
                    # print("Dealer BUST Win !")
                    break

            if not terminated:
                if player.score > dealer.score:
                    # print("Player scores more Win !")
                    reward = 1
                    delta = reward + 0 - sarsa.Q_S_A(state, Agent.STICK)
                    sarsa.update(delta)
                    terminated = True
                elif player.score < dealer.score:
                    # print("Dealer scores more Lose !")
                    reward = -1
                    delta = reward + 0 - sarsa.Q_S_A(state, Agent.STICK)
                    sarsa.update(delta)
                    terminated = True
                else:
                    # print("Draw !")
                    reward = 0
                    delta = reward + 0 - sarsa.Q_S_A(state, Agent.STICK)
                    sarsa.update(delta)
                    terminated = True
                    # player.print_holds()
                    # print()
                    # dealer.print_holds()

                    # print("This game is over !")

    print("Training Over !")
    return sarsa.Q
