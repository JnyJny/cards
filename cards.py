#!/usr/bin/env python3

import random

class Deck:

    _spades = 0x1F0A1
    _hearts = 0x1F0B1
    _diamonds = 0x1F0C1
    _clubs = 0x1F0D1
    _suits = [_spades, _hearts, _diamonds, _clubs]

    def __init__(self):
        self.top = 0
                
    @property
    def cards(self):
        try:
            return self._cards
        except AttributeError:
            pass
        self._cards = [chr(s+i) for s in range(0x1F0A1, 0x1F0E1, 16) for i in range(0,13)]
        return self._cards

    def shuffle(self):
        """
        """
        random.shuffle(self.cards)
        self.top = 0

    def peek(self):
        """
        """
        return self.cards[self.top]

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
        except IndexError as e:
            pass
        
        raise StopIteration

    @property
    def played(self):
        return self.cards[:self.top]

class CardGame:
    def __init__(self):
        self.deck = Deck()

    def deal(self, n_cards, n_players):
        hands = [[] for p in range(n_players)]
        
        for n in range(n_cards):
            for hand in hands:
                hand.append(next(self.deck))
        return hands

    def play(self, n_players, do_shuffle=True):
        
        if do_shuffle:
            self.deck.shuffle()

class Poker(CardGame):

    def __init__(self):
        self.deck = Deck()


    def play(self, n_players=4, do_shuffle=True):

        super().play(n_players, do_shuffle)

        hands = self.deal(5, n_players=n_players)
        
        winner = max(hands)
        
        for p, hand in enumerate(hands):
            if hand == winner:
                print(f'Player {p} {hand} is the winner!')
            else:
                print(f'Player {p} {hand}')

class TwentyOne(CardGame):

    def play(self, n_players=4, do_shuffle=True):
        
        super().play(n_players, do_shuffle)

        winner = False

        hands = [[] for _ in range(n_players+1)]

        hidden = 0
        dealer = -1

        deal = self.deal(1, n_players+1)

        print("Dealing down cards")
        
        for p, hand in enumerate(hands):
            hand.append(deal[p][0])
            
            
        while not winner:

            for p, hand in enumerate(self.deal(1, n_players+1)):
                
                if sum(hands[p]) > 21: # skip busted players
                    continue
                hands[p].append(hand[0])
                print("Player {p}: {hands[p]}")
                if sum(hands[p]) > 21:
                    print(f"Player {p} busted: {sum(hands[p])}")
                

                
        
        


if __name__ == '__main__':

    poker = Poker()
    poker.play()
        
