import itertools
import random

class Cards:
    def __init__(self):
            self.Deck = self.CardSetup()

    def CardSetup(fun):
        Suit = ["♡", "♤", "♢", "♧"]
        Value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        Deck = list(itertools.product(Value, Suit))
        random.shuffle(Deck)
        return Deck

    def PopDeck(self):
        if self.Deck:
            return self.Deck.pop()
    

class Grid:
    def __init__(self, card_deck):
        self.card_deck = card_deck

    def GridSetup(self):
        rows = [1, 2, 3, 4]
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        Dock = []
        for row in rows:
            for col in columns:
                RC = ("%s%d" % (col, row)) 
                Value = self.card_deck.PopDeck()
                Dock.append((RC, Value))
                print(("%s%d" % (col, row)), end=" ")
            print()
        # one = Dock.index("A1")
        print(Dock)
        

Cardds = Cards()
Cardds.CardSetup()

GridS = Grid(Cardds)
GridS.GridSetup()

GridS.Dock.index("A1")


# x = 0
# while(x < 3):
#     print("*", end=" ")
#     x = x + 1

    