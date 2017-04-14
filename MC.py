import Agent
import Deck
import State
import RL
import utils

EPISODES = 30000

deck = Deck.Deck()

GAMES = []

MC = RL.Monte_Carlo_Control()
policy = RL.Epsilon_Greedy()



for k in range(EPISODES):
    player = Agent.Player(deck)
    dealer = Agent.Dealer(deck)

    game = State.Game()

    player.draw_black()
    dealer.draw_black()

    state = State.State(player, dealer)
    game.add_state(state)
    state.print_state()

    # Player 's turn
    while policy.action(state,k+1,MC) == Agent.HIT:
        player.draw()
        game.add_action(Agent.HIT)
        if player.score > 21 or player.score < 1: # Lose
            game.add_reward(-1)
            game.terminated = True
            MC.update(game)
            break
        game.add_reward(0)
        state=state.next_state(player,dealer)
        game.add_state(state)

    if not game.terminated:
        game.add_action(Agent.STICK)


    # Dealer 's turn only if game is not over
    if not game.terminated:
        while dealer.score < 17:
            dealer.draw()
            if dealer.score > 21 or dealer.score < 1: # Win
                game.add_reward(1)
                game.terminated = True
                MC.update(game)
                break

    # Compare the scores if not terminated
    if not game.terminated:
        if player.score > dealer.score:
            print("Player scores more Win !")
            game.add_reward(1)
        elif player.score < dealer.score:
            print("Dealer scores more Lose !")
            game.add_reward(-1)
        else:
            print("Draw !")
            game.add_reward(0)

        game.terminated = True
        MC.update(game)


    GAMES.append(game)

    player.print_holds()
    print()
    dealer.print_holds()

    print("This game is over !")

print("Over !")

state_value = MC.Q.max(axis=2)
utils.plot_value(state_value)