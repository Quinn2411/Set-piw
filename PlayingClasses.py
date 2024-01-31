class cards:
   def __init__(self,number,symbol,shading,colour):
      self._number=number
      self._symbol=symbol
      self._shading=shading
      self._colour=colour
   def __repr__(self):
      return self.number +" "+ self.symbol+" " + self.shading +" "+ self.colour
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
   @number.setter
   def number(self,number):
      if number in ["1","2","3"]:
         self._number=number
      else:
         print ("That's not a number")
   @symbol.setter
   def symbol(self,symbol):
      if symbol in ["diamond","wave","oval"]:
         self._symbol=symbol
      else:
         print ("That's not a symbol")
   @shading.setter
   def shading(self,shading):
      if shading in ["filled","empty","striped"]:
         self._shading=shading
      else: 
         print("That's not a type of shading")
   @colour.setter
   def colour(self, colour):
      if colour in ["green","purple","red"]:
         self._colour=colour
      else:
         print("That's not a colour")
import random
class Table:
   def __init__(self):
      self._table=[]
   def fill(self,other):
      card = Deck.pop(other)
      self._table.append(card)
      return self._table
   def setisnotfound(self,other):
      for i in range(0,3):
       self._table.pop(0)
      for i in range(0,3):
        Table.fill(self,other)
   def setisfound(self,other,other1,other2,other3):
      self._table.pop(int(other1)-1)
      self._table.pop(int(other2)-2)
      self._table.pop(int(other3)-3)
      for i in range(0,3):
         Table.fill(self,other)
      return self._table
   def newgame(self,other):
      for i in range(0,12):
         Table.fill(self,other)
   def __repr__(self):
      p=" ".join(str(e)for e in self._table)
      return p
   def __len__(self):
      return len(self._table)
class Deck:
   def __init__(self):
     self._cards=[]
     self.populate()
   def __repr__(self):
      p=" ".join(str(e)for e in self._cards)
      return p
   def __len__(self):
      return len(self._cards)
   def populate(self):
      number=["1","2","3"]
      symbol=["diamond","wave","oval"]
      shading=["filled","empty","striped"]
      colour=["green","purple","red"]
      self._cards=[cards(a,b,c,d) for a in number for b in symbol for c in shading for d in colour ]
      return self._cards
   def pop(self):
      newcard=self._cards.pop(0)
      return newcard
   def shuffle(self):
      for k in range(len(self._cards)-1,0,-1):
         random.shuffle(self._cards)

