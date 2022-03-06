from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.deck.drawtablecard()
        self.players = []
        self.done = False
        self.result = None
        self.player = None

    def addPlayer(self, name):
        player = Player(name, self)
        self.players.append(player)
        if self.player is None:
            self.player = player
        return player

    def get_next_player(self):
        if self.players.index(self.player) + 1 < len(self.players):
            next_player = self.players[self.players.index(self.player) + 1]
        else:
            next_player = self.players[0]
        return next_player

    def validmoves(self):
        tablecard = self.deck.cards[-1]
        actions = ["Draw"]
        for card in self.player.hand:

            if card.value == "Hornik":
                card.change = "Zelen"
                actions.append(card)
                card.change = "Cerven"
                actions.append(card)
                card.change = "Gula"
                actions.append(card)
                card.change = "Srdce"
                actions.append(card)

            elif (
                    (tablecard.suit == card.suit)
                    or (tablecard.value == card.value)
                    or card.value == "Eso"
                    and not card.value == "Hornik"
            ):
                actions.append(card)

        return actions

    def play(self, action):
        if action == "Draw":
            if len(self.deck.cards) <= 1:
                self.done = True
                self.result = "No card left for draw"
                return self
            self.player.draw()
            self.player = self.get_next_player()
            return self

        elif action.value == "VII":
            self.deck.cards.append(action)
            self.player.hand.remove(action)

            if len(self.deck.cards) - 3 < 1:
                self.done = True
                self.result = "No card left for 3 draw"
                return self
            next_player = self.get_next_player()
            next_player.draw()
            next_player.draw()
            next_player.draw()

        elif action.value == "Eso":
            self.deck.cards.append(action)
            self.player.hand.remove(action)
            if not self.player.hand:
                self.done = True
                self.result = f"{self.player} won"
                return self

            self.player = self.get_next_player()
            self.player = self.get_next_player()

            return self

        elif action.change:

            self.deck.cards.append(action)
            self.player.hand.remove(action)
            self.deck.cards[-1].suit = action.change

        else:
            self.deck.cards.append(action)
            self.player.hand.remove(action)

        if not self.player.hand:
            self.done = True
            self.result = f"{self.player.name} won"
            return self

        self.player = self.get_next_player()
        return self
