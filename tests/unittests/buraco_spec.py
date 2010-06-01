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

    def it_should_deal_11_cards_to_each_player(self):
        for player in self.players:
            len(player.hand) |should| be(11)

#    def it_should_have_the_stack_with_the_remaining_cards(self):
#        remaing_cards = 104 - (
#                        len(self.players) * 11 +
#                        len(self.buraco.pots[0]) +
#                        len(self.buraco.pots[1]) )
#        len(self.buraco.stack) |should| be_equal_to(remaing_cards)

    def it_should_initialize_with_2_pots_with_11_cards_each(self):
        for pots in self.buraco.pots:
            len(pots) |should| be(11)

    def it_should_raise_exception_when_number_of_players_is_invalid(self):
        players = [Player("Hugo")]
        (lambda: Buraco(players)) |should| throw(InvalidNumberOfPlayers)

