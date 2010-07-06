from lettuce import *
from should_dsl import *

from player import *
from buraco import Buraco
from card import Card

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
    world.game._current_player = world.player

@step(r'When I draw a card from the stock')
def when_i_draw_a_card_from_the_stock(step):
    world.player.draws_card(STOCK)

@step(r'And the discard pile has "(\d+)" cards')
def and_the_discard_pile_has_n_cards(step, n):
    for i in range(int(n)):
        card = Card('J', 'spades')
        world.game.discard_pile.append(card)

@step(r'When I draw from the discard pile')
def when_i_draw_a_card_from_the_discard_pile(step):
    world.player.draws_card(DISCARD_PILE)

@step(r'Then I should have "(\d+)" cards in my hand')
def then_i_should_have_n_more_card_in_my_hand(step, n):
    world.player.hand |should| have(int(n)).cards

