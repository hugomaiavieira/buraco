STOCK = 0
DISCARD_PILE = 1

class CardNotInHandError(Exception): pass

class Player(object):

    def __init__(self, _name):
        self.name = _name
        self.hand = []
        self.game = None

    def __str__(self):
        return "Player %s" %(self.name)

    def receive_card(self, card):
        self.hand.append(card)

    def set_game(self, game):
        self.game = game

    def draws_card(self, pile):
        if pile == STOCK:
            card = self.game.pop_stock_card()
            self.hand.append(card)
        elif pile == DISCARD_PILE:
            for card in self.game.discard_pile:
                self.hand.append(card)

    def discard(self, card):
        self.hand.remove(card)
        self.game.discard_pile.append(card)

