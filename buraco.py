from deck import Deck

class InvalidNumberOfPlayers(Exception):
    def __init__(self):
        self.msg = "The number of players must be 2, 3 or 4"

class Buraco(object):
    def __init__(self, _players):
        if (len(_players) < 2) or (len(_players) > 4):
            raise InvalidNumberOfPlayers()
        self.players = _players

        self.pots = []
        self.stock = []
        self.discard_pile = []

        self.let_players_know_me()
        self._deal_cards()
        self._current_player = self.players[0]

    def let_players_know_me(self):
        for player in self.players:
            player.set_game(self)

    def _deal_cards(self):
        deck = Deck()

        self.pots.append(deck.get_cards(11))
        self.pots.append(deck.get_cards(11))

        for times in range(11):
            for player in self.players:
                player.receive_card(deck.get_cards(1))

        self.stock = deck.get_all_cards()

    def current_player(self):
        return self._current_player

    def pop_stock_card(self):
        card = self.stock.pop()
        return card

