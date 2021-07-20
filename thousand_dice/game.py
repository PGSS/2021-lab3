from typing import List

from .player import Player
from .turn import Turn

class Game:
    WINNING_SCORE = 10000
    def __init__(self,players : List[Player]):
        self._players = players


    def is_winner(self):
        for p in self._players:
            if p.score >= Game.WINNING_SCORE:
                return p
        else:
            return None
                
    def play(self):
        winner = None

        while winner == None:

            for p in self._players:
                turn = Turn()
                p.play(turn)

                if not turn._scored_on_last:                    
                    print(f"{p.name} didn't score, their total: {p.score}")
                elif p.score == 0 and turn.turn_score < 1000:
                    print(f"{p.name} scored {turn.turn_score} but didn't meet the minium")
                elif p.score == 0 and turn.turn_score >= 1000:
                    p._score += turn.turn_score
                    print(f"{p.name} scored {turn.turn_score} and they're in the game")
                else:
                    p._score += turn.turn_score
                    print(f"{p.name} scored {turn.turn_score} and they're totalling {p.score}")

            winner = self.is_winner()

        print(f"Game over! Winner is {winner.name} with a score of {winner.score}")
        for p in self._players:
            print(f"Player {p.name} scored {p.score}")
