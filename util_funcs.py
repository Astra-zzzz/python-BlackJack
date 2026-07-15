

def parse_int(prompt):
    while True:
        try:
            return int(input(prompt))
        
        except ValueError:
            print("Invalid input, must be an int.")

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