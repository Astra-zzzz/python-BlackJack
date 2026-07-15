import os
import random
import time
from rich import print

Hand = []
wincounter = {"Player" : 0, "AI" : 0}



def parse_int(prompt):
    while True:
        try:
            return int(input(prompt))
        
        except ValueError:
            print("Invalid input, must be an int.")

def initialize_game(player, dealer):
    Hand.clear()
    player.hand.clear()
    dealer.hand.clear()
    for i in range(2):
        player.draw_card()
        dealer.draw_card()
    print_hands(player, dealer)

def print_hands(player, dealer, reveal=False):
    print("-" * 50)
    print("Dealer:")
    if reveal:
        dealer.show_hand()
    else:
        dealer.show_initial()

    print("\nPlayer:")
    player.show_hand()
    print()

def wincon(player, dealer):
    p_sum = player.hand_value()
    d_sum = dealer.hand_value()
    if p_sum > 21 and d_sum > 21:
        print("[yellow]\nBoth Bust!\nBut the House wins![/yellow]")
        print("-" * 50)
        wincounter["AI"] += 1            
        return False
    elif p_sum > 21:
        print("[yellow]\nYou Bust![/yellow]")
        print("-" * 50)
        wincounter["AI"] += 1
        return False
    elif d_sum > 21:
        print("[yellow]\nHouse Busts.\nYou Win![/yellow]")
        print("-" * 50)
        wincounter["Player"] += 1
        return False
    elif d_sum == p_sum:
        print("[yellow]\nPush.\nHouse Wins.[/yellow]")
        wincounter["AI"] += 1
        print("-" * 50)
        return False
    elif d_sum == 21:
        print("[yellow]\nHouse BlackJack!!\nYou Lose[/yellow]")
        print("-" * 50)
        wincounter["AI"] += 1
        return False
    elif p_sum == 21:
        print("[yellow]\nYou BlackJack!![/yellow]")
        print("-" * 50)
        wincounter["Player"] += 1
        return False
    elif p_sum < d_sum:
        print("[yellow]\nYou Lose[/yellow]")
        print("-" * 50)
        wincounter["AI"] += 1
        return False
    elif p_sum > d_sum:
        print("[yellow]\nYou Win[/yellow]")
        print("-" * 50)
        wincounter["Player"] += 1
        return False
    return True


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

    
def main():
    
    player = Player()
    dealer = AI()
    repeat = 1

    while repeat:
        os.system("cls")
        initialize_game(player, dealer)
        while True:
            choice = parse_int("Hit(0) or Stand(1): ")
            if not choice and player.hand_value() <= 21:
                player.draw_card()
                os.system("cls")
                print_hands(player, dealer)
                if player.hand_value() >= 21:
                    print("You can't hit anymore.\nPlease wait...")
                    time.sleep(1)
                    break
            elif choice:
                print("You've chosen Stand.\nPlease wait...")
                time.sleep(1)
                break

        
        os.system("cls")
        print_hands(player, dealer, True)
        time.sleep(1)

        if player.hand_value() <= 21:
            while dealer.stand_ai(player):
                dealer.hit_ai(player)
                os.system("cls")
                print_hands(player, dealer, True)
                time.sleep(1)
        
        wincon(player, dealer)
        repeat = parse_int("Again? Yes(1) or No(0): ")

    print("Wins:")
    print(f'Player: {wincounter["Player"]}')
    print(f'Dealer: {wincounter["AI"]}')

if __name__ == "__main__":
    main()



