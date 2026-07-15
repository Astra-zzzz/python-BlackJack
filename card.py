import random
from globals import Hand

class Card:

    SUITS = ["Spade", "Diamond", "Clubs", "Hearts"]
    SYMBOLS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.suit = random.choice(self.SUITS)
        self.symbol = random.choice(self.SYMBOLS)
        self.value = self.get_value()
    
    def get_value(self):
        match self.symbol:
            case "Ace":
                return 11
            case "Jack" | "Queen" | "King":
                return 10
            case _:
                return int(self.symbol)
        
    def __eq__(self, other):
        return (
            self.suit == other.suit
            and
            self.symbol == other.symbol
        )