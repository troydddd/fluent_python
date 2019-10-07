# -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    def __setitem__(self, pos, value):
        self._cards[pos] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, pos, val):
        self._cards.insert(pos, val)
