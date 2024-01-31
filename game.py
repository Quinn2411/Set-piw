from models import Deck, Table, Card
from set_logic import find_one_set, check_set

# defining variables for the main function
my_deck = Deck()
my_deck.shuffle()

my_table = Table()
my_table.new_game(my_deck)

# putting the input in an index to make the code runs smoother and is more userfriendly
def get_input_cards(table):
    try:
        index1, index2, index3 = input().split(",")
    except KeyboardInterrupt:
        exit()
    except:
        print("invalid input, try again in the form a,b,c")
        return None, None, None
        
    try:
        card1 = table[int(index1)-1]
        card2 = table[int(index2)-1]
        card3 = table[int(index3)-1]
        return card1, card2, card3
    except: 
        print("invalid input, try again in the form a,b,c")
        return None, None, None

player_points = 0
computer_points = 0

# letting the game repeat until all cards have been on the table once
while len(my_deck) > 0:
    print(my_table)
    print(len(my_deck))
    
    # using Try and except to deal with incorrect inputs, so it doesn't crash the game
    card1, card2, card3 = get_input_cards(my_table)
    if card1 == None:
        continue
    
    # checking if the given cards form a set
    if check_set(card1, card2, card3):
        player_points += 1
        print(f"congrats you got a point\n the score is now: computer: {computer_points}, player: {player_points}")
        my_table.remove_set(my_deck, card1, card2, card3)
    else:
        if find_one_set(my_table) != None:
            computer_points += 1
            print(f"the computer found a set, so the computer got a point\n the score is now: computer: {computer_points}, player: {player_points}")
            card1, card2, card3 = find_one_set(my_table)
            print(f"{card1}, {card2}, {card3}")
            
            my_table.remove_set(my_deck, card1, card2, card3)
        # failsafe incase of CAP_Set on table
        else: 
            print("there is no set")
            my_table.refresh(my_deck)    
