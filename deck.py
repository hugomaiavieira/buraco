from random import shuffle

class Deck(object):
    def __init__(self):
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        _cards = []
        for suit in suits:
            for i in range(2):
                for value in values:
                    _cards.append([suit, value])
        self.cards = _cards
        shuffle(self.cards)

    def get_cards(self, number):
        cards = []
        for times in range(number):
            card = self.cards.pop()
            cards.append(card)
        return cards

