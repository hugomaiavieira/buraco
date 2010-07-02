from lettuce import *
from should_dsl import *

from player import Player
from buraco import Buraco

@step(r'Given I am a player named "(.*)"')
def given_i_am_a_player_named_group1(step, name):
    world.player = Player(name)

@step(r'And I am on a game with "(.*)"')
def and_i_am_on_a_game_with(step, names):
    names = names.split(', ')
    players = []
    for name in names:
        players.append(Player(name))
    players.append(world.player)
    world.game = Buraco(players)

@step(r'And is my turn to play')
def and_is_my_turn_to_play(step):
    player = world.game.current_player()
    player |should| be(world.player)

@step(r'When I draw a card from the stock')
def when_i_draw_a_card_from_the_stock(step):
    pass

@step(r'Then this card should be in my Hand')
def then_this_card_should_be_in_my_hand(step):
    pass

