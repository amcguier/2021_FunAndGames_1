from .Cards import *

class GameError(Exception):
    """Raised when a player makes an invalid play"""
    pass

class GameState:

    def __init__(self):
        deck = Deck()
        self._player_deck = Deck(existing_cards=[])
        self._computer_deck = Deck(existing_cards=[])
        self._game_over = False
        self._winner = None
        while deck.count > 0:
            self._player_deck.add_to_top(deck.draw())
            self._computer_deck.add_to_top(deck.draw())
            

    @property
    def winner(self):
        return "Nobody" if self._winner == None else self._winner

    @property
    def is_over(self):
        return self._game_over 

    def try_flip(self):
        if self.is_over:
            raise GameError("Can't play when the game is over!")
        if self._player_deck.count == 0:
            self._game_over = True
            self._winner = "Computer"
            return None
        if self._computer_deck.count == 0:
            self._game_over = True
            self._winner = "Player"
            return None

        return (self._player_deck.draw(),self._computer_deck.draw())

    def add_to_player(self,cards):
        for card in cards:
            self._player_deck.add_to_bottom(card)

        if self._player_deck.count == 52:
            self._winner = "Player"
            self._game_over = True

    def add_to_computer(self,cards):
        for card in cards:
            self._computer_deck.add_to_bottom(card)

        if self._computer_deck.count == 52:
            self._winner = "Computer"
            self._game_over = True
