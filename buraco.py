from deck import Deck

class InvalidNumberOfPlayers(Exception):
    def __init__(self):
        self.msg = "The number of players must be 2, 3 or 4"

class Buraco(object):
    def __init__(self, _players):
        if (len(_players) < 2) or (len(_players) > 4):
            raise InvalidNumberOfPlayers()
        self.players = _players
        self.deck = Deck()

    def distribute_cards(self):
        for times in range(11):
            for player in self.players:
                player.receive_card(self.deck.get_cards(1))

