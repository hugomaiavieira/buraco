class Player(object):
    def __init__(self, _name):
        self.name = _name
        self.cards = []

    def receive_card(self, card):
        self.cards.append(card)

