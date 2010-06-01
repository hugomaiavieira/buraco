from freshen import *
from should_dsl import *

from player import Player
from buraco.buraco import *

@Given(r'I have the players (.*)')
def given_i_have_the_players(names):
    names = names.split(', ')
    scc.players = []
    for name in names:
        scc.players.append(Player(name))

@When(r'I initialize the game')
def when_i_initialize_the_game():
    try:
        scc.buraco = Buraco(scc.players)
    except InvalidNumberOfPlayers as e:
        scc.msg = e.msg

@Then(r'each player has 11 cards')
def then_each_player_has_11_cards():
    for player in scc.players:
        len(player.hand) |should| be_equal_to(11)

@Then(r'the game cannot be started')
def the_game_cannot_be_started():
    scc.msg |should_be.equal_to| "The number of players must be 2, 3 or 4"

@Then(r'the game has 2 pots with 11 cards each')
def the_game_has_2_pots_with_11_cards_each():
    for pots in scc.buraco.pots:
        len(pots) |should| equal_to(11)

