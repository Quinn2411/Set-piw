from Check_Set import check_set, checkelement
from Card import cards, Deck

table = [Deck.Draw]
setsontable = []
#Writing a function to find sets
def findset():
    
    for card1 in table:
        for card2 in table:
            for card3 in table:
                if card1 != card2 and card2 != card3 and card1 != card3:
                    if check_set(card1, card2, card3) == True: 
                        #Returns set to a list of all sets on the table.
                        setsontable.append([card1, card2, card3])
                        #Confirms we dont have a CAP set on the table
                        return True
    #Confirms we have a CAP set on the table
    return False
print(setsontable)