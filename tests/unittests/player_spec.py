import unittest
from should_dsl import *
from ludibrio import Dummy
from player import Player

class PlayerSpec(unittest.TestCase):
    def it_should_initialize_with_the_name(self):
        player = Player("Ronaldo")
        player.name |should| be("Ronaldo")

    def it_should_receive_cards(self):
        player = Player("Ronaldo")
        card = Dummy()
        player.receive_card(card)
        len(player.cards) |should| be(1)

        for times in range(10):
            player.receive_card(card)
        len(player.cards) |should| be(11)

