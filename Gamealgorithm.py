from Card import Deck, Table, cards
from findoneset import findoneset
from Check_Set import check_set, checkelement
#Defining variables for the main function
Mydeck=Deck()
Deck.shuffle(Mydeck)
Mytable=Table()
Table.newgame(Mytable,Mydeck)

def main(deck, table):
    #Letting the game repeat until all cards have been on the table once
    while len(Mydeck) > 0:
        print(Mytable)
        print(len(Mydeck))
        index1,index2, index3 = input().split(",")
        #Putting the input in an index to make the code runs smoother and is more userfriendly
        def inputforcards(tableyourusing):
            card1 = tableyourusing._table[int(index1)-1]
            card2=tableyourusing._table[int(index2)-1]
            card3=tableyourusing._table[int(index3)-1]
            return card1,card2,card3
        cardv1,cardv2,cardv3=inputforcards(Mytable)
        #Checking if the given cards form a set
        def whogetsapoint(deck, table, card1, card2, card3):
            if check_set(cardv1,cardv2,cardv3)==True:
                print("congrats you got a point!")
                
                Mytable.setisfound(Mydeck,k[0],k[1],k[3])
            else:
                if findoneset(Mytable) != None:
                    
                    print('the computer found a set, so the computer got a point')
                    k=findoneset(Mytable)
                    print(k)
                    Mytable.setisfound(Mydeck,k[0],k[1],k[2])
                    #Failsafe incase of CAP_Set on table
                else: 
                    print("idd leeg")
                    Mytable.setisnotfound(Mydeck)    
            return Mytable
            #Making sure the whogetsapoint function runs
        updatedtable = whogetsapoint(Mydeck, Mytable, cardv1, cardv2, cardv3)
    return Mytable

print (main(Mydeck, Mytable))

 


