import random

from .player import Player
from .turn import Turn


class ComputerPlayer(Player):

    def __init__(self, name):
        id = random.randint(1,500)
        super().__init__(f"{name} - {id}")

class Conservative(ComputerPlayer):

    def __init__(self):
        super().__init__("Conservative")

    def play(self, turn : Turn):
        while turn.turn_score == 0 or (turn.turn_score < 1000 and self.score):
            dice = turn.roll()
            scored_dice = []
            if Turn.is_straight(dice):
                scored_dice.extend(dice)
            else:
                group_dice = Turn.get_triples(dice)
                scored_dice.extend(group_dice)
                for d in group_dice:
                    dice.remove(d)
                scored_dice.extend(Turn.get_ones(dice))
                scored_dice.extend(Turn.get_fives(dice))

            if len(scored_dice) > 0:
                turn.hold_dice(scored_dice)
            else:
                return

class Aggressive(ComputerPlayer):
    def __init__(self):
        super().__init__("Aggressive")

    def play(self, turn: Turn):
        while True:
            dice = turn.roll()
            scored_dice = []
            if Turn.is_straight(dice):
                scored_dice.extend(dice)
            else:
                group_dice = Turn.get_triples(dice)
                scored_dice.extend(group_dice)
                for d in group_dice:
                    dice.remove(d)
                scored_dice.extend(Turn.get_ones(dice))
                scored_dice.extend(Turn.get_fives(dice))

            if len(scored_dice) > 0:
                turn.hold_dice(scored_dice)
                remaining = len(dice) - len(scored_dice)
                step_down = self.score > 1000 and remaining > 0 and remaining <= 2
                new_turn = turn.turn_score >= 1000 and self.score < 1000

                if step_down or new_turn:
                    return
                
            else:
                return
        
