from freshen import *
from should_dsl import *

from player import Player
from buraco.buraco import Buraco

@Given(r'I have the players (.*)')
def given_i_have_the_players(names):
    names = names.split(', ')
    scc.players = []
    for name in names:
        scc.players.append(Player(name))

@When(r'I initialize the game')
def when_i_initialize_the_game():
    scc.buraco = Buraco(scc.players)
    scc.buraco.distribute_cards()

@Then(r'each player has 11 cards')
def then_each_player_has_11_cards():
    for player in scc.players:
        len(player.cards) |should_be.equal_to| 11

