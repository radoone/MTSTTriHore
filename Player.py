class Player:
    def __init__(self, name, game):
        self.name = name
        self.hand = []
        self.game = game

    def draw(self):
        self.hand.append(self.game.deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
        print("# cards" + self.name + " " + str(len(self.hand)))

    def play(self, action):
        return self.game.play(action)

    def validmoves(self):
        return self.game.validmoves()