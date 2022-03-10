import copy

from Card import Card
from Deck import Deck
from Player import Player


class TriHoreState:

    def __init__(
            self, current_player: Player, players, tablecard: object, played_cards: object, uncovered_cards: object):
        self.game_result_value = None
        self.result = None
        self.done = False
        self.played_cards = played_cards
        self.tablecard = tablecard
        self.current_player = current_player
        self.players = players
        self.deck = Deck()
        self.deck.cards
        self.deck.cards.append(tablecard)
        self.uncovered_cards = uncovered_cards
        self.deck.cards += uncovered_cards + played_cards
        print("Start------------------------------------------------")
        print(
            f'Hrac: {self.current_player.name}  Karty:{self.current_player.hand} "Na stole: " {self.tablecard}')

    @property
    def get_legal_actions(self):

        actions = ["Draw"]

        for card in self.current_player.hand:
            if card.value == "Hornik":
                card.change = "Zelen"
                actions.append(copy.copy(card))
                card.change = "Cerven"
                actions.append(copy.copy(card))
                card.change = "Gula"
                actions.append(copy.copy(card))
                card.change = "Srdce"
                actions.append(copy.copy(card))
                del card.change
            elif (
                    (self.tablecard.suit == card.suit)
                    or (self.tablecard.value == card.value)
                    or card.value == "Eso"
                    and not card.value == "Hornik"
            ):
                actions.append(card)
        print(f"Actions: {actions}")
        return actions

    @property
    def is_game_over(self):
        if not self.current_player.hand:
            return True
        return False

    @property
    def game_result(self):
        if self.current_player == self.player and self.game_result_value is not None:
            return self.game_result_value
        elif not self.current_player == self.player and self.game_result_value is not None and not self.game_result_value == 0:
            return -1

    @property
    def get_next_player(self):
        if self.players.index(self.current_player) + 1 < len(self.players):
            next_player = self.players[self.players.index(self.current_player) + 1]
        else:
            next_player = self.players[0]
        return next_player

    def move(self, action):
        print("Action: {0}".format(action))
        if action == "Draw":
            if not len(self.deck.cards):
                self.done = True
                self.result = "No card left for draw"
                self.game_result_value = 0
                return TriHoreState(
                    current_player=self.current_player,
                    players=self.players,
                    tablecard=self.tablecard,
                    played_cards=self.played_cards,
                    uncovered_cards=self.uncovered_cards
                )
            self.current_player.draw()
            self.current_player = self.get_next_player
            return TriHoreState(
                current_player=self.current_player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards
            )

        elif action.value == "VII":
            self.deck.cards.append(action)
            self.current_player.hand.remove(action)

            if not len(self.deck.cards) - 3:
                self.done = True
                self.result = "No card left for 3 draw"
                self.game_result_value = 0
                return TriHoreState(
                    current_player=self.current_player,
                    players=self.players,
                    tablecard=self.tablecard,
                    played_cards=self.played_cards,
                    uncovered_cards=self.uncovered_cards
                )
            next_player = self.get_next_player
            next_player.draw()
            next_player.draw()
            next_player.draw()

        elif action.value == "Eso":
            self.played_cards.append(action)
            self.current_player.hand.remove(action)
            if not self.current_player.hand:
                self.done = True
                self.result = f"{self.current_player} won"
                self.game_result_value = 1
                return TriHoreState(
                    current_player=self.current_player,
                    players=self.players,
                    tablecard=self.tablecard,
                    played_cards=self.played_cards,
                    uncovered_cards=self.uncovered_cards
                )

            self.current_player = self.get_next_player
            self.current_player = self.get_next_player

            return TriHoreState(
                current_player=self.current_player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards
            )

        elif hasattr(action, 'change'):
            self.tablecard.suit = action.change
            self.deck.played_cards.append(action)

            for card in self.current_player.hand:
                if card.value == action.value and card.suit == action.suit:
                    self.current_player.hand.remove(card)

        else:
            self.played_cards.append(action)
            self.current_player.hand.remove(action)

        if not self.current_player.hand:
            self.done = True
            self.result = f"{self.current_player.name} won"
            self.game_result_value = 1
            return TriHoreState(
                current_player=self.current_player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards
            )

        self.current_player = self.get_next_player
        return TriHoreState(
            current_player=self.current_player,
            players=self.players,
            tablecard=self.tablecard,
            played_cards=self.played_cards,
            uncovered_cards=self.uncovered_cards
        )
