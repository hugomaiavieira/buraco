import unittest
from should_dsl import *

from deck import Deck

class DeckSpec(unittest.TestCase):

    def it_initially_should_have_104_cards(self):
        deck = Deck()
        len(deck.cards) |should| be(104)

    def it_should_return_n_card(self):
        deck = Deck()
        deck.get_cards(1)
        len(deck.cards) |should_be| be(103)

        deck.get_cards(17)
        len(deck.cards) |should| be(86)

