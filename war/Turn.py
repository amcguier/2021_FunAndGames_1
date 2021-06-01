from enum import Enum
from .Game_State import *

class TurnState(Enum):
    Initial = 1
    IsWar = 2
    WarFlipped = 3
    PlayerWon = 4
    PlayerLost = 5
    TurnEnded = 6    
    Done = 7
    

class Turn():
    
    def __init__(self,game_state : GameState):
        self._game_state = game_state
        self._state = TurnState.Initial
        self._pile = []
        self._my_card = None
        self._opponent_card = None

    def _set_winner_from_string(self,winner):
        if winner == "Computer":
            self._state = TurnState.PlayerLost
        else:
            self._state = TurnState.PlayerWon
            
    def flip_card(self):
        if self.state not in [TurnState.Initial, TurnState.WarFlipped]:
            raise GameError("It's not time to flip a card right now!")

        flip_result = self._game_state.try_flip()
        if flip_result != None:
            (self._my_card, self._opponent_card) = flip_result
            self._pile.append(self._my_card)
            self._pile.append(self.opponent_card)
            
            if self._my_card.rank == self._opponent_card.rank:
                self._state = TurnState.IsWar
                print( f"War! You: {self._my_card} Computer: {self._opponent_card}")
            elif self._my_card.rank > self._opponent_card.rank:                
                self._state = TurnState.PlayerWon
                print( f"You win the hand! You: {self._my_card} Computer: {self._opponent_card}")
            else:
                self._state = TurnState.PlayerLost
                print( f"You lose the hand! You: {self._my_card} Computer: {self._opponent_card}")

        else:
            self._set_winner_from_string(self._game_state.winner)

    def flip_war_card(self):
        if self.state != TurnState.IsWar:
            raise GameError("You can't do a war unless you're tied after the flip!")
        
        flip_result = self._game_state.try_flip()        
        if flip_result != None:
            self._pile.append(flip_result[0])
            self._pile.append(flip_result[1])
            self._state = TurnState.WarFlipped
        else:
            self._set_winner_from_string(self._game_state.winner)

    def pickup_pile(self):
        if self.state != TurnState.PlayerWon:
            raise GameError("You can't cheat and pick up cards you didn't win!")
        self._game_state.add_to_player(self._pile)
        self._pile.clear()
        self._state = TurnState.TurnEnded

    def congratulate_opponent(self):
        if self.state != TurnState.PlayerLost:
            raise GameError("You can't congratulate your opponent unless they won!")
        self._state = TurnState.TurnEnded

    @property
    def state(self):
        return self._state
    
    @property
    def my_card(self):
        return self._my_card

    @property
    def opponent_card(self):
        return self._opponent_card

    def end_turn(self):
        if self.state != TurnState.TurnEnded:
            raise GameError("You can't end your turn yet!") 
        self._game_state.add_to_computer(self._pile)
        self._pile.clear()
        self._game_state = TurnState.Done
        
