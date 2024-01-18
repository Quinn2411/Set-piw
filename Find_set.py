from Check_Set import check_set, checkelement
from Card import cards, Deck

#Writing a function to find sets
def findset(table):
    setsontable = []    
    for i, card1 in enumerate(table):
        for j, card2 in enumerate(table[i:]):
            for k, card3 in enumerate(table[j:]):
                if card1 != card2 and card2 != card3 and card1 != card3:
                    if check_set(card1, card2, card3) == True: 
                        #Returns set to a list of all sets on the table.
                        setsontable.append([card1, card2, card3])
                        
    return setsontable

table = [cards("1","diamond", "filled", "purple"),
cards("1","diamond", "filled", "red"),
cards("1","diamond", "filled", "green")]

setsontable = findset(table)
print(setsontable)

