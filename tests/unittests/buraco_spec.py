import unittest
from should_dsl import *

from player import Player
from buraco import *

class BuracoSpec(unittest.TestCase):

    def setUp(self):
        self.players = [Player("Hugo"), Player("Pedro")]
        self.buraco = Buraco(self.players)

    def it_should_initialize_the_game_with_given_players(self):
        self.buraco.players |should| have(self.players[0])
        self.buraco.players |should| have(self.players[1])

    def it_should_distribute_11_cards_to_each_player(self):
        self.buraco.distribute_cards()
        for player in self.players:
            len(player.cards) |should| be(11)

    def it_should_raise_exception_when_number_of_players_is_invalid(self):
        players = [Player("Hugo")]
        (lambda: Buraco(players)) |should| throw(InvalidNumberOfPlayers)
#        self.assertRaises(InvalidNumberOfPlayers, Buraco, players)

