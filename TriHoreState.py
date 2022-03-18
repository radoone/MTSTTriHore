import copy
from typing import Set

import Card
from Player import Player


class TriHoreState:
    def __init__(self, current_player: Player, player: Player, players: list, tablecard: Card.Card, played_cards: set,
                 uncovered_cards: set):
        self.player = player
        self.game_result_value = None
        self.result = None
        self.done = False
        self.played_cards = played_cards
        self.tablecard = tablecard
        self.current_player = current_player
        self.players = players
        self.uncovered_cards = uncovered_cards

        print("Start------------------------------------------------")
        print(f'Hrac: {self.current_player.name} ')
        print(f'Karty: {self.current_player.hand} ')
        print(f'"Na stole: " {self.tablecard}')
        print(f' V nezname karty:{self.uncovered_cards} ')
        print(f'zname karty:{self.played_cards} ')

        count: int = 0
        for player in self.players:
            if isinstance(player.hand, set):
                count += len(player.hand)
            else:
                count += 1

        pocet_kariet: int = len(self.uncovered_cards) + len(self.played_cards) + count + 1
        print(f'Pocet kariet: {pocet_kariet}')
        assert 32 == pocet_kariet, f'Miznu Karty{pocet_kariet}'
        return

    def get_actions(self, card: Card.Card, actions: set = Card.Card) -> set:
        if card.value == "Hornik":
            card.change = "Zelen"
            actions.add(copy.copy(card))
            card.change = "Cerven"
            actions.add(copy.copy(card))
            card.change = "Gula"
            actions.add(copy.copy(card))
            card.change = "Srdce"
            actions.add(copy.copy(card))
            del card.change
        elif (
                (self.tablecard.suit == card.suit)
                or (self.tablecard.value == card.value)
                or card.value == "Eso"
                and not card.value == "Hornik"
        ):
            actions.add(card)
        print(f"Actions: {actions}")
        return actions

    @property
    def get_legal_actions(self):
        actions: set[Card] = {"Draw"}
        if isinstance(self.current_player.hand, set):
            for card in self.current_player.hand:
                actions = actions.union(self.get_actions(card, actions))


        elif isinstance(self.current_player.hand, Card.Card):
            actions.extend(self.get_actions(self.current_player.hand, actions))
        return actions

    def is_game_over(self):
        if not self.current_player.hand:
            return True
        return False

    def game_result(self):
        if self.game_result_value is not None:
            if self.game_result_value == 0:
                return 0
            elif self.current_player == self.player:
                return self.game_result_value
            elif not self.current_player == self.player:
                return -1
            elif not self.current_player == self.player and self.game_result_value:
                return -1

    def get_next_player(self) -> Player:
        if self.players.index(self.current_player) + 1 < len(self.players):
            next_player = self.players[self.players.index(self.current_player) + 1]
        else:
            next_player = self.players[0]
        return next_player

    def draw(self):
        # TODO: random get ?
        if len(self.uncovered_cards) > 0:
            card = self.uncovered_cards.pop()
        elif len(self.played_cards) > 0:
            card = self.played_cards.pop()
        else:
            raise Exception("No card to draw")
        return card

    def move(self, action):
        if self.game_result_value:
            return

        print("Action: {0}".format(action))
        if action == "Draw":
            if not len(self.played_cards) + len(self.uncovered_cards):
                self.done = True
                self.result = "No card left for draw"
                self.game_result_value = 0
                return TriHoreState(
                    current_player=self.current_player,
                    player=self.player,
                    players=self.players,
                    tablecard=self.tablecard,
                    played_cards=self.played_cards,
                    uncovered_cards=self.uncovered_cards
                )
            self.current_player.hand.add(self.draw())
            self.current_player = self.get_next_player()
            return TriHoreState(
                current_player=self.current_player,
                player=self.player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards
            )

        # elif action.value == "VII":
        #
        #     self.played_cards.add(self.tablecard)
        #     self.tablecard = action
        #     self.current_player.hand.remove(action)
        #
        #     if not len(self.played_cards) + len(self.uncovered_cards) - 3:
        #         self.done = True
        #         self.result = "No card left for 3 draw"
        #         self.game_result_value = 0
        #         return TriHoreState(
        #             current_player=self.current_player,
        #             player=self.player,
        #             players=self.players,
        #             tablecard=self.tablecard,
        #             played_cards=self.played_cards,
        #             uncovered_cards=self.uncovered_cards
        #         )
        #     next_player: Player = self.get_next_player()
        #
        #     self.players[self.players.index(next_player)].hand = self.draw()
        #     self.players[self.players.index(next_player)].hand = self.draw()
        #     self.players[self.players.index(next_player)].hand = self.draw()
        #
        #     #next_player.hand = self.draw()
        #     #next_player.hand = self.draw()
        #     #next_player.hand = self.draw()
        #
        #     self.current_player = self.get_next_player()
        #     return TriHoreState(
        #         current_player=self.current_player,
        #         player=self.player,
        #         players=self.players,
        #         tablecard=self.tablecard,
        #         played_cards=self.played_cards,
        #         uncovered_cards=self.uncovered_cards
        #     )

        elif action.value == "Eso":
            self.played_cards.add(action)
            self.current_player.hand.remove(action)
            if not self.current_player.hand:
                self.done = True
                self.result = f"{self.current_player} won"
                print(self.result)
                self.game_result_value = 1
                return TriHoreState(
                    current_player=self.current_player,
                    players=self.players,
                    tablecard=self.tablecard,
                    played_cards=self.played_cards,
                    uncovered_cards=self.uncovered_cards,
                    player=self.player
                )

            self.current_player = self.get_next_player()
            self.current_player = self.get_next_player()

            return TriHoreState(
                player=self.player,
                current_player=self.current_player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards
            )

        elif hasattr(action, 'change'):
            self.tablecard.suit = action.change
            self.played_cards.add(action)

            cardlist = list(self.current_player.hand)

            for card in cardlist:
                if card.value == action.value and card.suit == action.suit:
                    cardlist.remove(card)

            self.current_player.hand = set(cardlist)

        else:
            self.played_cards.add(action)
            self.current_player.hand.remove(action)

        if not self.current_player.hand:
            self.done = True
            self.result = f"{self.current_player.name} won"
            print(self.result)
            self.game_result_value = 1
            return TriHoreState(
                current_player=self.current_player,
                players=self.players,
                tablecard=self.tablecard,
                played_cards=self.played_cards,
                uncovered_cards=self.uncovered_cards,
                player=self.player
            )

        self.current_player = self.get_next_player()
        return TriHoreState(
            current_player=self.current_player,
            player=self.player,
            players=self.players,
            tablecard=self.tablecard,
            played_cards=self.played_cards,
            uncovered_cards=self.uncovered_cards
        )
