from check_set import check_set

# writing a function to find one set on the table
def find_one_set(A):
    # making use of enumerate to skip checking duplicates (if card1, card2, card3 is checked we dont check card1, card3 , card2 aswell)
    for i, card1 in enumerate(A._table): 
        for j, card2 in enumerate(A._table[i:]):
            for k, card3 in enumerate(A._table[j:]):
                if card1 != card2 and card2 != card3 and card1 != card3:
                    if check_set(card1, card2, card3): 
                        return card1, card2, card3
