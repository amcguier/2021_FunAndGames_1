from .Turn import Turn
from .Game_State import * 



class Game:    
    def __init__(self,player_method):
        self._player_method = player_method
        self._game_state = GameState()

    def take_turn(self):
        if not self.game_over:
            turn = Turn(self._game_state)
            self._player_method(turn)

    @property
    def game_over(self):
        return self._game_state.is_over

    @property
    def winner(self):
        return self._game_state.winner
