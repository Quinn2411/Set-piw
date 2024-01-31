from PlayingClasses import Deck, Table, cards
from FINDONESET import findoneset
from Check_Set import check_set, checkelement
Mydeck=Deck()
Deck.shuffle(Mydeck)
Mytable=Table()
Table.newgame(Mytable,Mydeck)

def main(deck, table):
    
    while len(Mydeck) > 0:
        
        print(Mytable)
        print(len(Mydeck))
        index1,index2, index3 = input().split(",")
        def inputforcards(tableyourusing):
            card1 = tableyourusing._table[int(index1)-1]
            card2=tableyourusing._table[int(index2)-1]
            card3=tableyourusing._table[int(index3)-1]
            return card1,card2,card3
        cardv1,cardv2,cardv3=inputforcards(Mytable)
        def whogetsapoint(deck, table, card1, card2, card3):
            if check_set(cardv1,cardv2,cardv3)==True:
                print("congrats you got a point!")
                
                Mytable.setisfound(Mydeck,cardv1,cardv2,cardv3)
                return True
            else:
                if findoneset(Mytable) != []:
                    
                    print('the computer found a set, so the computer got a point')
                    k=findoneset(Mytable)
                    print(k)
                    Mytable.setisfound(Mydeck,k[0],k[1],k[2])
                    return False
                else: 
                    print("idd leeg")
                    Mytable.setisnotfound(Mydeck)
            print(len(Mydeck))    
            return Mytable
        
        updatedtable = whogetsapoint(Mydeck, Mytable, cardv1, cardv2, cardv3)
   
    return Mytable
