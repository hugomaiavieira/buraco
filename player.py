STOCK = 0
DISCARD_PILE = 1

class Player(object):

    def __init__(self, _name):
        self.name = _name
        self.hand = []
        self.game = None

    def receive_card(self, card):
        self.hand.append(card)

    def set_game(self, game):
        self.game = game

    def draws_card(self, pile):
        if pile == STOCK:
            card = self.game.pop_stock_card()
            self.hand.append(card)
        elif pile == DISCARD_PILE:
            pass

    def discard(self, card):
        self.hand.remove(card)
        self.game.discard_pile.append(card)

