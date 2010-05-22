from freshen import *

from player import Player
from buraco.buraco import Buraco

@Given(r'I have (\d+) players, with names (.*)')
def given_i_have_a_player_named(number, names):
    names = names.split(', ')
    scc.players = []
    for name in names:
        scc.players.append(Player(name))

@When(r'I initialize the game')
def when_i_initialize_the_game():
    scc.buraco = Buraco(scc.players)

@Then(r'the cards are distributed')
def then_each_player_has_11_cards():
    scc.buraco.distribute_cards()

