from deck import Deck

TOP=1
BOTTOM=0

class InvalidNumberOfPlayers(Exception):
    def __init__(self):
        self.msg = "The number of players must be 2, 3 or 4"

class Buraco(object):
    def __init__(self, _players):
        if (len(_players) < 2) or (len(_players) > 4):
            raise InvalidNumberOfPlayers()
        self.players = _players
        self.deck = Deck()
        self.pots = []
        self.stack = []

        self.__deal_cards__()

    def __deal_cards__(self):
        self.pots.append(self.deck.get_cards(11))
        self.pots.append(self.deck.get_cards(11))
        for times in range(11):
            for player in self.players:
                player.receive_card(self.deck.get_cards(1))
        card = self.deck.get_cards(1)
        while(card != None):
            self.stack.append(card)
            card = self.deck.get_cards(1)

        len(self.deck)

