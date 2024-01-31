# importing random so we can use it later on in the shuffle function
import random

# defining a class for the cards in set so that it is possible to compare card properties
class Card:
     # every card has four attributes: colour, number, shading and symbol which define the card
    def __init__(self, number, symbol, shading, colour):
        self._number = number
        self._symbol = symbol
        self._shading = shading
        self._colour = colour
   
    def __repr__(self):
        return self.number + " " + self.symbol + " " + self.shading + " " + self.colour
  
    # creating the properties, so that we can easily update the variables if we need to
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
   
    # giving the properties attributes
    @number.setter
    def number(self, number):
        if number in ["1", "2", "3"]:
            self._number = number
        else:
            print("That's not a number")
    
    @symbol.setter
    def symbol(self, symbol):
        if symbol in ["diamond", "squiggle", "oval"]:
            self._symbol = symbol
        else:
            print("That's not a symbol")
    
    @shading.setter
    def shading(self, shading):
        if shading in ["filled", "empty", "shaded"]:
            self._shading = shading
        else: 
            print("That's not a type of shading")
   
    @colour.setter
    def colour(self,  colour):
        if colour in ["green", "purple", "red"]:
            self._colour = colour
        else:
            print("That's not a colour")

# Table class for the cards in play
class Table:
    def __init__(self):
        self._table = []
   
    # a basic fill fuction we can use in a lot of the other functions
    def fill(self, deck):
        card = deck.pop()
        self._table.append(card)
        return self._table
  
    def __getitem__(self, key):
        return self._table[key]

    # refreshing the table after player input in the case that there is no set
    def refresh(self, deck):
        for i in range(0, 3):
            self._table.pop(0)
        for i in range(0, 3):
            self.fill(deck)
             
    # a function to describe what to do if either the computer or the player found a set, that removes the cards that form a set, and fills it with new cards
    def remove_set(self, deck, card1, card2, card3):
        self._table.remove(card1)
        self._table.remove(card2)
        self._table.remove(card3)
        for i in range(0, 3):
            self.fill(deck)
        return self._table
    
    # drawing 12 cards from the deck
    def new_game(self, deck):
        for i in range(0, 12):
            self.fill(deck)
    
    def __repr__(self):
        p = "\n".join(str(e)for e in self._table)
        return p
    
    def __len__(self):
        return len(self._table)
    
# making a deck so the game doesn't prolong infinitely
class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
    
    def __repr__(self):
        p = " ".join(str(e)for e in self._cards)
        return p
   
    def __len__(self):
        return len(self._cards)
    # a populate function, so we can fill the deck
    def populate(self):
        number = ["1", "2", "3"]
        symbol = ["diamond", "squiggle", "oval"]
        shading = ["filled", "empty", "shaded"]
        colour = ["green", "purple", "red"]
        # use the list comprehensions for the built- in function list, so that we can fill the deck in one line
        self._cards = [Card(a, b, c, d) for a in number for b in symbol for c in shading for d in colour]
    
    def pop(self):
        return self._cards.pop()
    # shuffling the deck by using the random.shuffle method for lists from the random module
    def shuffle(self):
        for k in range(len(self._cards)-1, 0, -1):
            random.shuffle(self._cards)

