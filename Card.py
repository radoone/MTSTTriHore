class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.change = None

    def __str__(self):
        return f"{self.value}, {self.suit}, {self.change}"

    def show(self):
        print(f"{self.value}, {self.suit}", end=" ")
