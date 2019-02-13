#Cody Dzierzon
#2/19


import random

class Card(object):
    """a playing card.
    this class will vuld a single card
    to build a card call Card() and class in a rank and a suit
    card1 = Card(rank = "A", suit ="s")"""
    ranks = ["A","2", "3","4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    suits = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = True

    def flip(self):
        self.faceup = not self.face_up

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """A hand of playing cards.
    this class will allow for you to add cards to your hand from the deck:
    for i in range (5):
    my_hand.add(deck.pop())
    your_hand.add(deck.pop())
    it will allow you to give your cards to someone else:
    my_hand.give(my_hand.cards[0],your_hand)
    and it will allow for you to clear your hand:
    my_hand.clear()
your_hand.clear()"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep
    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A deck of playing cards."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positionable_Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")

class Positionable_Card(card):
    """ a card that can be face up or face down"""
    def __init__ (self, rank,suit,face_up=True):
        super(Positionable_Card, self). __init__(rank,suit)
        self.is_face_up=face_up

    def _str_(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit")







































# #main
# card1 = Card(rank = "A",suit="C")
# print ("printing card object")
# print(card1)
# card2 = Card(rank="2",suit="C")
# card3 = Card(rank="3",suit="C")
# card4 = Card(rank="4",suit="C")
# card5 = Card(rank="5",suit="C")
# print(card2)
# print(card3)
# print(card4)
# print(card5)
#
#
#
# my_hand = Hand()
# your_hand = Hand()
# deck = []
# for i in range(10):
#     card = Card(rank = random.choice(Card.ranks),suit = random.choice(Card.suits))
#     deck.append(card)
#
# for i in range (5):
#     my_hand.add(deck.pop())
#     your_hand.add(deck.pop())
# print(my_hand)
# print(your_hand)
#
# my_hand.give(my_hand.cards[0],your_hand)
# print(my_hand)
# print(your_hand)
#
# my_hand.clear()
# your_hand.clear()
#
# print(my_hand)
# print(your_hand)