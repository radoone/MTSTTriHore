from random import  randint

from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.puttedcards = []

    def build(self):
        for v in ["Zelen", "Cerven", "Gula", "Srdce"]:
            for s in ["VII", "VII", "IX", "X", "Dolnik", "Hornik", "Kral", "Eso"]:
                self.cards.append(Card(v, s))

    def shuffle(self):
        for i in range(1, len(self.cards)):
            r = randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

    def drawtablecard(self):
        self.cards.append(self.drawCard())

    def put(self, Card):
        self.cards.append(Card)