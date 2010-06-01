import unittest
from should_dsl import *

from deck import Deck

class DeckSpec(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def it_initially_should_have_104_cards(self):
        len(self.deck.cards) |should| be(104)

    def it_should_return_n_card(self):
        self.deck.get_cards(1)
        len(self.deck.cards) |should_be| be(103)

        self.deck.get_cards(17)
        len(self.deck.cards) |should| be(86)

        self.deck.get_cards(87) |should| be(None)

    def it_should_return_the_number_os_cards(self):
        len(self.deck) |should| be(104)

        self.deck.get_cards(5)
        len(self.deck) |should| be(99)

