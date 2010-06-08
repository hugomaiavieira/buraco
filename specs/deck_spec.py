import unittest
from should_dsl import *

from deck import Deck

class DeckSpec(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def it_initially_should_have_104_cards(self):
        self.deck |should| have(104).cards

    def it_should_return_n_card(self):
        self.deck.get_cards(1)
        self.deck |should| have(103).cards

        self.deck.get_cards(17)
        self.deck |should| have(86).cards

        self.deck.get_cards(87) |should| be(None)

    def it_should_return_the_number_os_cards(self):
        self.deck |should| have(104).cards

        self.deck.get_cards(5)
        self.deck |should| have(99).cards

