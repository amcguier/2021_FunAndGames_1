from war.Game import Game
from war.Turn import Turn
from war.Turn import TurnState

def do_war(turn):
    raise NotImplementedError

def play_war(turn):
    raise NotImplementedError

if __name__ == "__main__":
    game = Game(play_war)
    while not game.game_over:
        game.take_turn()
        
    print("Game Over Winner Is:", game.winner)
