from util_funcs import print_hands
from globals import wincounter, Hand
from rich import print



def initialize_game(player, dealer):
    Hand.clear()
    player.hand.clear()
    dealer.hand.clear()
    for i in range(2):
        player.draw_card()
        dealer.draw_card()
    print_hands(player, dealer)

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