from PlayingClasses import Deck, Table, cards
from FINDONESET import findoneset
from Check_Set import check_set, checkelement
#Defining variables for the main function
Mydeck=Deck()
Deck.shuffle(Mydeck)
Mytable=Table()
Table.newgame(Mytable,Mydeck)

def main(deck, table):
    points = 0
    computerpoints = 0
    #Letting the game repeat until all cards have been on the table once
    while len(Mydeck) > 0:
        print(Mytable)
        print(len(Mydeck))
        #Using Try and except to deal with incorrect inputs, so it doesn't crash the game
        try:
            index1,index2, index3 = input().split(",")
        except:
            print("invalid input, try again in the form a,b,c")
            exit() 
        #Putting the input in an index to make the code runs smoother and is more userfriendly
        def inputforcards(tableyourusing):
            try:
                card1 = tableyourusing._table[int(index1)-1]
                card2=tableyourusing._table[int(index2)-1]
                card3=tableyourusing._table[int(index3)-1]
                return card1,card2,card3
            except: 
                print("invalid input, try again in the form a,b,c")
                exit()

        cardv1,cardv2,cardv3=inputforcards(Mytable)
        #Checking if the given cards form a set
        
        if check_set(cardv1,cardv2,cardv3)==True:
            points += 1
            print("congrats you got a point, the score is now ",points,computerpoints)
            Mytable.setisfound([Mydeck,index1,index2,index3])
        else:
            if findoneset(Mytable) != None:
                computerpoints += 1
                print("the computer found a set, so the computer got a point, the score is now ",points, computerpoints)
                k=findoneset(Mytable)
                print(k)
                
                Mytable.setisfound(Mydeck,k[0],k[1],k[2])
                #Failsafe incase of CAP_Set on table
            else: 
                print("idd leeg")
                Mytable.setisnotfound(Mydeck)    
            
          
        
    return Mytable

print (main(Mydeck, Mytable))

 



print (main(Mydeck, Mytable))

 


