from random import randint
from typing import List, Any

from Card import Card


class Deck:
    cards: list[Card]

    def __init__(self):
        self.cards = []
        self.played_cards = {}
        self.table_card: Card = None

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

    def drawCard(self) -> Card:
        return self.cards.pop()

    def drawTableCard(self) -> Card:
        self.table_card = self.drawCard()
        return self.table_card

    def put(self, card):
        self.cards.append(card)
