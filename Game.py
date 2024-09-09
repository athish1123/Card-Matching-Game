import itertools
# import random

class Cards:
    def CardSetup(fun):
        Suit = ["♡", "♤", "♢", "♧"]
        Value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        Deck = list(itertools.product(Value, Suit))
        print(Deck)

Cardds = Cards()
Cardds.CardSetup()
