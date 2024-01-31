# comparing all elements of the cards
def check_set(card1, card2, card3):
    colour_check = check_element(card1.colour, card2.colour, card3.colour)
    symbol_check = check_element(card1.symbol, card2.symbol, card3.symbol)
    shading_check = check_element(card1.shading, card2.shading, card3.shading)
    number_check = check_element(card1.number, card2.number, card3.number)
    return colour_check and symbol_check and number_check and shading_check

# to check if a specific dimension of the card is allowed to form a set
def check_element(property1, property2, property3):
    if property1 == property2 and property2 == property3:
        return True
    elif property1 != property2 and property2 != property3 and property1 != property3:
        return True
    return False

