import unittest
from should_dsl import *

from card import Card

class CardSpec(unittest.TestCase):

    def it_should_have_a_value_and_a_suit(self):
        card = Card('J', 'spades')
        card.value |should| equal_to('J')
        card.suit |should| equal_to('spades')

