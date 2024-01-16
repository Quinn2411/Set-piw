






#Comparing all elements of the cards
def check_set():
    number_check = checkelement (Card1.number, Card2.number, Card3.number)
    shape_check = checkelement (Card1.shape, Card2.shape, Card3.shape)
    pattern_check = checkelement (Card1.pattern, Card2.pattern, Card3.pattern)
    colour_check = checkelement (Card1.colour, Card2.colour, Card3.colour)
    if colour_check == True and shape_check == True and number_check == True and pattern_check == True:
        return True
    return False

#To check if a specific dimension of the card is allowed to form a set
def checkelement(property1, property2, property3):
    if property1 == property2 and property2 == property3:
        return True
    elif property1 != property2 and property2 != property3 and property1 != property3:
        return True
    return False
