from card import Card
from globals import Hand
from rich import print

class Player:
    def __init__(self):
        self.hand = []
        self.sum = 0

    def draw_card(self):
        while True:
                temp = Card()
                if not any(temp == cards for cards in Hand): 
                    Hand.append(temp)
                    break
        self.hand.append(Hand[-1])

    def hand_value(self):
        self.sum = sum(values.value for values in self.hand)
        if self.sum > 21 and any(check.symbol == "Ace" for check in self.hand):
            for card in self.hand:
                if card.symbol == "Ace" and card.value == 11:
                    card.value = 1
                    self.sum -= 10
                    if self.sum <= 21:
                        break
        return self.sum

    def show_hand(self):
        for card in self.hand:
            print(f"[blue]{card.symbol}[/blue] of {card.suit}")

class AI(Player):

    def show_initial(self):
        print(f"[blue]{self.hand[0].symbol}[/blue] of {self.hand[0].suit}")
        print("[red]Hidden[/red]")
    
    def hit_ai(self, player):
        self.hand_value()
        if player.sum > self.sum and self.sum < 21 and player.sum <= 21:
            self.draw_card()

    def stand_ai(self, player):
        self.hand_value()
        player.hand_value()

        if self.sum >= 21:
            return 0
        elif self.sum >= player.sum:
            return 0
        else:
            return 1