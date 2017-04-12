import Agent
import Deck


deck = Deck.Deck()

player=Agent.Player()
dealer = Agent.Dealer()

player.draw_black(deck)
dealer.draw_black(deck)

