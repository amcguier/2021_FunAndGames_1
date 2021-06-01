import random

class Card():
    def __init__(self, rank,suit):
        self._suit = suit
        self.icon # trigger value error if suit is invalid
        self._rank = rank
        self.rank_string #trigger value error if rank is invalid

    def __eq__(self,other):
        if isinstance(other,self.__class__):
            return self.rank == other.rank and self.suit == other.suit
        else:
            return False

    def __ne__(self,other):
        return not (self == other)
    
    @property
    def suit(self):
        return self._suit            
    
    @property
    def icon(self):
        if self.suit == "Diamond":
            return "♢"
        elif self.suit == "Spade":
            return "♤"
        elif self.suit == "Club":
            return "♧"
        elif self.suit == "Heart":
            return "♡"
        else:
            raise ValueError("Invalid suit in card")

    @property
    def rank(self):
        return self._rank
        
    @property
    def rank_string(self):
        if self._rank > 1 and self._rank < 11:
            return str(self._rank)
        elif self._rank == 11:
            return "Jack"
        elif self._rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        elif self.rank == 14:
            return "Ace"
        else:
            raise ValueError("Invalid rank provided", self._rank)
        
    def __str__(self):
        return self.rank_string + " of " + self.icon

    def print(self):
        return self.__str__


class Deck():

    def _create_empty_deck():
        cards = []

        suits = ["Heart","Club","Diamond", "Spade"]

        for suit in suits:
            for i in range(2,15):
                cards.append(Card(i,suit))

        
        random.shuffle(cards)
        return cards
    
    def __init__(self,existing_cards = None):
        if existing_cards == None:
            self._cards = Deck._create_empty_deck()
        else:
            self._cards = existing_cards
                    
    @property
    def count(self):
        return len(self._cards)

    def draw(self,count = None):
        if len(self._cards) == 0:
            raise ValueError("Insufficient cards to make that draw")
        else:
            return self._cards.pop()

    def draw_multiple(self,to_draw):
        if to_draw > len(self._cards):
            raise ValueError("Insufficient cards to make that draw")
        else:
            cards = []
            for i in range(0,to_draw):
                cards.append(self.draw())                           
            return cards
        
    def add_to_bottom(self,card):
        self._cards.append(card)

    def add_to_top(self,card):
        self._cards.insert(0,card)
        
