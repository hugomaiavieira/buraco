import unittest
from should_dsl import *

from deck import Deck

class DeckSpec(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def it_initially_should_have_104_cards(self):
        self.deck |should| have(104).cards

    def it_should_return_one_card(self):
        self.deck.get_cards()
        self.deck |should| have(103).cards

        self.deck.get_cards()
        self.deck |should| have(102).cards

    def it_should_return_the_number_of_cards_as_his_length(self):
        len(self.deck) |should| be(104)

        self.deck.get_cards()
        len(self.deck) |should| be(103)

