#coding:utf-8

import unittest
from should_dsl import *

from player import *
from card import Card
from buraco import *

class BuracoSpec(unittest.TestCase):

    def setUp(self):
        self.hugo = Player("Hugo")
        self.pedro = Player("Pedro")
        self.players = [self.hugo, self.pedro]
        self.buraco = Buraco(self.players)

    def it_should_initialize_the_game_with_given_players(self):
        self.buraco.players |should| include(self.players[0])
        self.buraco.players |should| include(self.players[1])
        self.buraco |should| have(2).players

    def it_should_deal_11_cards_to_each_player(self):
        for player in self.players:
            player.hand |should| have(11).cards

    def it_should_initialize_with_2_pots_with_11_cards_each(self):
        for pots in self.buraco.pots:
            pots |should| have(11).cards

    def it_should_raise_exception_when_number_of_players_is_invalid(self):
        players = [Player("Hugo")]
        (lambda: Buraco(players)) |should| throw(InvalidNumberOfPlayers)

    def it_should_let_the_players_know_that_they_belongs_to_me(self):
        ronaldo = Player("Ronaldo")
        ze = Player("Zé")
        game = Buraco([ronaldo, ze])
        ronaldo.game |should| be(game)

    def it_should_pop_card_from_the_stock(self):
        stock_length = len(self.buraco.stock)
        card = self.buraco.pop_stock_card()
        card |should| be_kind_of(Card)
        len(self.buraco.stock) |should| equal_to(stock_length - 1)

    def it_should_return_the_player_of_the_current_turn(self):
        self.hugo.hand = []
        self.buraco.current_player() |should| be(self.hugo)
        # shot
        self.hugo.draws_card(STOCK)
        self.hugo.discard(self.hugo.hand[0])
        # after his move, the turn goes to the next player in the table
        self.buraco.current_player() |should| be(self.pedro)

