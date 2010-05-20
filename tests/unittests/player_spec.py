import unittest
from should_dsl import *

from player import Player

class PlayerSpec(unittest.TestCase):
    def it_should_initialize_with_the_name(self):
        player = Player("Ronaldo")
        player.name |should_be.equal_to| "Ronaldo"

