from PlayingClasses import Deck, Table, cards
from FINDONESET import findoneset
from check_set import check_set, check_element
Mydeck=Deck()
points=0
computerpoints = 0
Deck.shuffle(Mydeck)
Mytable=Table()
Table.newgame(Mytable,Mydeck)
print(Mytable)
index1,index2, index3 = input().split(",")
def inputforcards(tableyourusing):
    card1 = tableyourusing._table[int(index1)-1]
    card2=tableyourusing._table[int(index2)-1]
    card3=tableyourusing._table[int(index3)-1]
    return card1,card2,card3
cardv1,cardv2,cardv3=inputforcards(Mytable)



   
if check_set(cardv1,cardv2,cardv3)==True:
    print("congrats you got a point!")
    points+=1
    Mytable.setisfound(Mydeck,cardv1,cardv2,cardv3)
else:
    #print("unfortunately that's not a set, try again")
    if findoneset(Mytable) != []:
        computerpoints += 1
        print('the computer found a set, so the computer got a point')
        k=findoneset(Mytable)
        print(k)
        Mytable.setisfound(Mydeck,k[0],k[1],k[2])
    else: 
        print("idd leeg")
        Mytable.setisnotfound(Mydeck)

print(Mytable) 

