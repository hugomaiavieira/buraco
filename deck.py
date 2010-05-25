class Deck(object):
    def __init__(self):
        naipes = ['espadas', 'copas', 'ouro', 'paus']
        _cards = []
        for naipe in naipes:
            for i in range(2):
                for numero in range(13):
                    _cards.append([naipe, numero])
        self.cards = _cards


    def get_cards(self, number):
        cards = []
        for times in range(number):
            card = self.cards.pop()
            cards.append(card)
        return cards

