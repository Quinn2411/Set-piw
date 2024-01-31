#importing random so we can use it later on in the sufflefunction
import random
#Defining a class for the cards in set so that it is possible to compare card properties
class cards:
   #everycard has four atributes: colour, number,shading and symbol wich difine the card
   def __init__(self,number,symbol,shading,colour):
      self._number=number
      self._symbol=symbol
      self._shading=shading
      self._colour=colour
   def __repr__(self):
      return self.number +" "+ self.symbol+" " + self.shading +" "+ self.colour
   #Creating the properties, so that we can easily update the veriables if we need to do
   @property
   def number(self):
      return self._number
   @property
   def symbol(self):
      return self._symbol
   @property
   def shading(self):
      return self._shading
   @property
   def colour(self):
      return self._colour
   #Giving the properties attributes
   @number.setter
   def number(self,number):
      if number in ["1","2","3"]:
         self._number=number
      else:
         print ("That's not a number")
   @symbol.setter
   def symbol(self,symbol):
      if symbol in ["diamond","squiggle","oval"]:
         self._symbol=symbol
      else:
         print ("That's not a symbol")
   @shading.setter
   def shading(self,shading):
      if shading in ["filled","empty","shaded"]:
         self._shading=shading
      else: 
         print("That's not a type of shading")
   @colour.setter
   def colour(self, colour):
      if colour in ["green","purple","red"]:
         self._colour=colour
      else:
         print("That's not a colour")


#TableClass for the cards in play
class Table:
   def __init__(self):
      self._table=[]
   # a basic fill fuction we can use in a lot of the other functions
   def fill(self,other):
      card = Deck.pop(other)
      self._table.append(card)
      return self._table
   #a function to describe what the algorithm needs to do if there is not a set, while using the fill function we defind above
   def setisnotfound(self,other):
      for i in range(0,3):
       self._table.pop(0)
      for i in range(0,3):
        Table.fill(self,other)
   # a function to describe what to do if either the computer or the player found a set,using the place of the card on the table using the fill function we defined above
   def setisfound(self,other,other1,other2,other3):
      self._table.pop(int(other1)-1)
      self._table.pop(int(other2)-2)
      self._table.pop(int(other3)-3)
      for i in range(0,3):
         Table.fill(self,other)
      return self._table
   #Drawing 12 cards from the deck
   def newgame(self,other):
      for i in range(0,12):
         Table.fill(self,other)
   def __repr__(self):
      p=" ".join(str(e)for e in self._table)
      return p
   def __len__(self):
      return len(self._table)
#Making a deck so the game doesn't prolong infinitely
class Deck:
   def __init__(self):
     self._cards=[]
     self.populate()
   def __repr__(self):
      p=" ".join(str(e)for e in self._cards)
      return p
   def __len__(self):
      return len(self._cards)
   # a populate function, so we can fil the deck
   def populate(self):
      number=["1","2","3"]
      symbol=["diamond","squiggle","oval"]
      shading=["filled","empty","shaded"]
      colour=["green","purple","red"]
      #use the listcomprensions for the built- in function list, so that we can fill the deck in one line
      self._cards=[cards(a,b,c,d) for a in number for b in symbol for c in shading for d in colour ]
      return self._cards
   def pop(self):
      newcard=self._cards.pop(0)
      return newcard
   #shuffling the deck by using the random.shuffle method for lists from the module random
   def shuffle(self):
      for k in range(len(self._cards)-1,0,-1):
         random.shuffle(self._cards)

