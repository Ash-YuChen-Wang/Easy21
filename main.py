import Agent
import Deck
import State
import RL

deck = Deck.Deck()

GAMES = []

for i in range(3):
    player = Agent.Player(RL.Ask_user,deck)
    dealer = Agent.Dealer(RL.Until_17,deck)

    game = State.Game()

    player.draw_black()
    dealer.draw_black()

    state = State.State(player, dealer)
    state.add_to_game(game)
    state.print_state()

    # Player 's turn
    while player.action():
        state = state.next_state(player, dealer)
        state.add_to_game(game)  # You should only add your state to game when it's player's turn
        state.print_state()
        if state.player_terminal():
            print("Player BUST !")
            game.reward = -1
            break

    # Dealer 's turn only if game is not over
    if not game.reward:
        while dealer.action():
            state = state.next_state(player, dealer)
            state.print_state()
            if state.dealer_terminal():
                print("Dealer BUST !")
                game.reward = 1
                break

    # Compare the scores only if game is not over
    if not game.reward:
        if player.score > dealer.score:
            print("Player scores more Win !")
            game.reward = 1
        elif player.score < dealer.score:
            print("Dealer scores more Lose !")
            game.reward = -1
        else:
            print("Draw !")
            game.reward = 0

    GAMES.append(game)

    player.print_holds()
    print()
    dealer.print_holds()

    print("This game is over !")
