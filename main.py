from thousand_dice.computer import *
from thousand_dice.player import Player
from thousand_dice.turn import Turn
from thousand_dice.game import Game


class HumanPlayer(Player):

    def __init__(self):
        super().__init__("Your Player Name")


    #challenge
    # don't use the Turn. methods to figure out what dice you
    # have, calculate the scores yourself!
        
    def play(self, turn : Turn):
        ## Functions you can call

        # turn.roll()   returns a list of dice rolled
        # turn.hold_dice(list_of_dice) save dice you've used
        # turn.turn_score    #accumulated points so far

        # self.score     # your current score

        # Turn.is_straight(list_dice) # returns True or False if the included dice are a straight
        # Turn.get_triples(list_dice) # returns a list containing all the triples of dice in the provided list
        # Turn.get_ones(list_dice) # returns a list containing all the 1's in the
        # Turn.get_fives(list_dice) # returns a list of dice containing all the 5's in the provided list
        pass



if __name__ == "__main__":
    ## to add your player add , HumanPlayer() to the list below
    players = [Conservative(), Aggressive()]
    game = Game(players)
    game.play()
