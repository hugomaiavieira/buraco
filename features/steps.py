from lettuce import *
from should_dsl import *

from player import Player
from buraco import *

@step(r'I have the players (.*)')
def given_i_have_the_players(step, names):
    names = names.split(', ')
    world.players = []
    for name in names:
        world.players.append(Player(name))

@step(r'I initialize the game')
def when_i_initialize_the_game(step):
    try:
        world.buraco = Buraco(world.players)
    except InvalidNumberOfPlayers as e:
        world.msg = e.msg

@step(r'each player has 11 cards')
def then_each_player_has_11_cards(step):
    for player in world.players:
        len(player.hand) |should| equal_to(11)

@step(r'the game cannot be started')
def the_game_cannot_be_started(step):
    world.msg |should_be.equal_to| "The number of players must be 2, 3 or 4"

@step(r'the game has 2 pots with 11 cards each')
def the_game_has_2_pots_with_11_cards_each(step):
    for pots in world.buraco.pots:
        len(pots) |should| equal_to(11)

@step(r'the game has the stack with (\d+)')
def the_game_has_the_stack_with(step, ramaining_cards):
    ramaining_cards = int(ramaining_cards)
    len(world.buraco.stack) |should| equal_to(ramaining_cards)

