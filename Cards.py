from Card import Card


class Cards:
    def __init__(self):
        self.cards = None
        self.cards = []
        self.build()

    def build(self):
        for v in ["Zelen", "Cerven", "Gula", "Srdce"]:
            for s in ["VII", "VII", "IX", "X", "Dolnik", "Hornik", "Kral", "Eso"]:
                self.cards.append(Card(v, s))
