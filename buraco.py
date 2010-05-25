from deck import Deck

class Buraco(object):
    def __init__(self, _players):
        self.players = _players
        self.deck = Deck()

    def distribute_cards(self):
        for times in range(11):
            for player in self.players:
                player.receive_card(self.deck.get_cards(1))

