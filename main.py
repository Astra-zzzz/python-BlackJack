import os
import time
from rich import print
from util_funcs import print_hands, parse_int
from hands import Player, AI
from game_mechanics import wincon, initialize_game
from globals import wincounter


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
