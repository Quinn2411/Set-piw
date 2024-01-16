






#Comparing all elements of the cards
def check_set():
    number_check = checkelement (Card1.number, Card2.number, Card3.number)
    symbol_check = checkelement (Card1.symbol, Card2.symbol, Card3.symbol)
    shading_check = checkelement (Card1.shading, Card2.shading, Card3.shading)
    colour_check = checkelement (Card1.colour, Card2.colour, Card3.colour)
    if colour_check == True and symbol_check == True and number_check == True and shading_check == True:
        return True
    return False

#To check if a specific dimension of the card is allowed to form a set
def checkelement(property1, property2, property3):
    if property1 == property2 and property2 == property3:
        return True
    elif property1 != property2 and property2 != property3 and property1 != property3:
        return True
    return False
