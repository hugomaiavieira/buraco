#coding:utf-8

import unittest
from should_dsl import *
from ludibrio import Dummy
from player import *
from buraco import Buraco
from card import Card

class PlayerSpec(unittest.TestCase):

    def setUp(self):
        self.hugo = Player("Hugo")
        self.pedro = Player("Pedro")
        self.game = Buraco([self.hugo, self.pedro])

    def it_should_be_represented_by_his_name(self):
        self.hugo.__str__() |should| equal_to('Player Hugo')
        self.pedro.__str__() |should| equal_to("Player Pedro")

    def it_should_initialize_with_the_name(self):
        self.hugo.name |should| equal_to("Hugo")

    def it_should_receive_cards(self):
        ronaldo = Player("Ronaldo")
        card = Dummy()
        ronaldo.receive_card(card)
        ronaldo.hand |should| have(1).card

        for times in range(10):
            ronaldo.receive_card(card)
        ronaldo.hand |should| have(11).cards

    def it_should_set_his_game(self):
        self.pedro.set_game(self.game)
        self.pedro.game |should| be(self.game)

    def it_should_draw_a_card_from_the_stock(self):
        self.hugo.draws_card(STOCK)
        self.hugo.hand |should| have(12).cards

    def it_should_draw_a_card_from_the_discard_pile(self):
        card = Card('Q', 'spades')
        self.game.discard_pile.append(card)
        self.hugo.draws_card(DISCARD_PILE)
        self.hugo.hand |should| have(12).cards

    def it_should_discard_the_given_card(self):
        card = Card('J', 'spades')
        self.pedro.hand.append(card)
        self.pedro.discard(card)
        self.pedro.hand |should| have(11).cards
        self.pedro.hand |should_not| contain(card)
        self.game.discard_pile |should| contain(card)

    def it_should_not_allow_user_to_discard_a_card_if_he_doesnt_have_it(self):
        self.pedro.hand = []
        card = Card('J', 'spades')
        (lambda: self.pedro.discard(card)) |should| throw(CardNotInHandError)

    def after_discarding_the_player_should_notify_the_game_he_is_done(self):
        pass

