class Player(object):
    def __init__(self, _name):
        self.name = _name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

