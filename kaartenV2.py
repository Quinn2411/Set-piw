import random
class cards:
   def __init__(self,colour,symbol,shading,number):
      self._number=number
      self._symbol=symbol
      self._shading=shading
      self._colour=colour
   def __repr__(self):
      return self.number + self.symbol + self.shading + self.colour
   @property
   def number(self):
      return self._number
   @property
   def symbool(self):
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
   @symbool.setter
   def symbool(self,symbool):
      if symbool in ["diamond","wave","oval"]:
         self._symbol=symbol
      else:
         print ("That's not a symbool")
   @shading.setter
   def shading(self,shading):
      if shading in ["filled","empty","stripped"]:
         self._shading=shading
      else: 
         print("That's not a type of shading")
   @colour.setter
   def colour(self, colour):
      if colour in ["green","purple","red"]:
         self._colour=colour
      else:
         print("That's not a colour")
from kaarten import kaarten
class Deck:
   
      
   def __init__(self):
     self._cards=[]
     self.populate()
     print(self._cards)
   def __len__(self):
      return len(self._cards)
   def populate(self):
      number=["1","2","3"]
      symbool=["diamond","wave","oval"]
      shading=["filled","empty","stripped"]
      colour=["green","purple","red"]
      self._cards=[cards(a,b,c,d) for a in number for b in symbool for c in shading for d in colour ]
      return self._cards
   def shuffle(self):
      for k in range(len(self._cards)-1,0,-1):
         random.shuffle(self._cards)
      print(my_deck)
   
      
my_deck=Deck()
Deck.shuffle(my_deck)
