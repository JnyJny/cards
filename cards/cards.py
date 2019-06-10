"""
"""

from enum import IntEnum

class Suits(IntEnum):
    spades = 0x1f0a1
    hearts = 0x1f0b1
    diamonds = 0x1f0c1
    clubs = 0x1f0d1

class Faces(IntEnum):
    ace = 0
    two = 1
    three = 2
    four = 3
    five = 4
    six = 5
    seven = 6
    eight = 7
    nine = 8
    jack = 9
    queen = 10
    king = 11
    joker = 15

class Card:
    @classmethod
    def joker(cls):
        return cls(0, 0x1f0cf)
    
    def __init__(self, suit : Suits, face: Faces) -> None:
        self.suit = suit
        self.face = face

    def __str__(self):
        return chr(self.suit+self.face)

