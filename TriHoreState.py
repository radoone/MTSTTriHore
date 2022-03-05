class TriHoreState:
    def __init__(
            self, current_player="Jozko", tablecard=None, hand="", played_cards=None
    ):
        if played_cards is None:
            played_cards = []
        if tablecard is None:
            tablecard = ["E", "G"]
        self.current_player = current_player
        self.tablecard = tablecard
        self.hand = hand
        self.played_cards = played_cards
        self.uncovered_cards = self.getuncoveredcards()

    def getuncoveredcards(self):
        # TODO: Implement
        return []

    def get_legal_actions(self):
        # TODO: Implement
        return [1, 2, 3]

    def is_game_over(self):
        # TODO: Implement
        return False

    def move(self,action):
        # TODO: Implement
        return TriHoreState()
