"""simulates a deck of playing cards
"""

import random
from enum import IntEnum
from .card import Suits, Faces, Card

class Deck:
    """A deck of playing cards.
    """

    def __init__(self, seed: int = 0, use_jokers=False):
        """
        :param int seed:
        :param bool use_jokers:

        """
        self.seed = seed
        self.use_jokers = use_jokers
        self.top = 0
        random.seed(self.seed)
        

    def __repr__(self):
        repr_str = '{}(seed={}, use_jokers={})'
        return repr_str.format(self.__class__.__name__,
                               self.seed,
                               self.use_jokers)

    def __str__(self):
        return ''.join([str(c) for c in self.cards])
                
    @property
    def cards(self):
        """A list of 52 (54 if jokers enabled) .Card objects.
        """
        try:
            return self._cards
        except AttributeError:
            pass

        self._cards = []
        
        for suit in Suits:
            for face in Faces:
                if face == Faces.JOKER and not self.use_jokers:
                    continue
                self._cards.append(Card(suit, face))
                                   
        return self._cards
    

    def shuffle(self, seed=None):
        """Shuffle the deck.
        :param int seed:
        """
        
        if seed:
            random.seed(seed)
            
        random.shuffle(self.cards)
        self.top = 0


    def peek(self):
        """Returns the top card without dealing it from the deck.
        """
        return self.cards[self.top]

    def __contains__(self, other):
        """
        """
        return other in self.cards

    def __iter__(self):
        """
        """
        self.top = 0
        return self

    def __next__(self):
        """
        """
        try:
            top_card = self.cards[self.top]
            self.top += 1
            return top_card
        except IndexError:
            pass
        
        raise StopIteration

    @property
    def played(self):
        """A list of cards that have been dealt from the deck.
        """
        return self.cards[:self.top]

    def deal(self, ncards, nplayers):
        """
        :param int ncards:
        :param int nplayers:
        :return: List[List[str]]
        """
        
        hands = [[] for _ in range(nplayers)]

        for n in range(ncards):
            for hand in hands:
                 hand.append(next(self))


        return hands
