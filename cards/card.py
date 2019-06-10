"""a playing card
"""

from enum import IntEnum

class Suits(IntEnum):
    SPADES = 0x1f0a1
    HEARTS = 0x1f0b1
    DIAMONDS = 0x1f0c1
    CLUBS = 0x1f0d1

_JOKER_SUIT= 0x1f0c0

class Faces(IntEnum):
    ACE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    JOKER = 15

class Card:
    """Cards have a suit and face value.
    """
    
    @classmethod
    def joker(cls):
        """Returns a Card configured as a joker.
        """
        return cls(_JOKER_SUIT, Faces.JOKER)
    
    def __init__(self, suit : Suits, face: Faces) -> None:
        self.suit = suit
        self.face = face
        if self.face == Faces.JOKER:
            self.suit = _JOKER_SUIT
            self.face = face

    def __repr__(self):
        repr_str = '{}(suit={}, face={})'
        return repr_str.format(self.__class__.__name__,
                               self.suit,
                               self.face)

    def __str__(self):
        return chr(self.suit+self.face)

    @property
    def is_joker(self):
        """
        """
        return self.suit == _JOKER_SUIT and self.face == Faces.JOKER

    @property
    def is_ace(self):
        """
        """
        return self.face == Faces.ACE


