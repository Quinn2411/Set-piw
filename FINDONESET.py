from testfile import check_set
#Writing a function to find one set on the table
def findoneset(A):
    for i, card1 in enumerate(A._table): #Making use of enumerate to skip checking duplicates (If Card1,Card2,Card3 is checked we dont check Card1,Card3,Card2 also)
        for j, card2 in enumerate(A._table[i:]):
            for k, card3 in enumerate(A._table[j:]):
                if card1 != card2 and card2 != card3 and card1 != card3:
                    if check_set(card1, card2, card3) == True: 
                        #Indexing for ease of use
                        indexcard1=A._table.index(card1)+1     
                        indexcard2=A._table.index(card2)+1    
                        indexcard3=A._table.index(card3)+1
                        indexforset=[indexcard1,indexcard2,indexcard3]
                        return indexforset