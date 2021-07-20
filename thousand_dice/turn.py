import itertools
import functools

from typing import List, Set
from uuid import UUID

from .dice import Dice
from .game_error import GameError


class Turn:
    straight = [1,2,3,4,5,6]
    
    def __init__(self):
        self._dice: List[Dice] = [Dice() for x in range(6)]
        self._ids: Set[UUID] = set()
        for d in self._dice:
            self._ids.add(d.id)
        self._held: Set[Dice] = set()
        self._can_roll = True
        self._turn_score = 0
        self._scored_on_last = False
        
    def roll(self):
        self._scored_on_last = False
        if not self._can_roll:
            raise GameError("You aren't allowed to roll right now!")

        to_return = []
        
        for dice in self._dice:
            if not dice.is_locked:
                dice.roll()
                dice._lock()
                to_return.append(dice)

            self._can_roll = False

        return to_return
            
    @property
    def turn_score(self):
        return self._turn_score

    
    
    def calc_score(dice: List[Dice]):
        lst = list(dice)
        lst.sort(key=lambda x: x.current_value)

        # check for a straight, rarest combination
        if len(lst) == 6 and Turn.straight == [x.current_value for x in lst]:
            return 1500
            

        # now check for 3 of a kind

        grps = itertools.groupby(list(lst), key=lambda x: x.current_value)

        accumulated_score = 0
        
        for key,group in grps:
            group_list = list(group)
            if len(group_list) == 6:
                score = 1000 if key == 1 else 100 * key
                score *= 2
                return score
            elif len(group_list) >= 3:
                accumulated_score += 1000 if key == 1 else 100*key
                print("Grouping", lst)
                for x in group_list[:3]:
                    lst.remove(x)
                print("Grouping post remove", lst)

        for x in lst:
            if x.current_value == 1:
                accumulated_score += 100
            elif x.current_value == 5:
                accumulated_score += 50
            else:
                raise GameError("You can't score with regular dice!", lst)

        return accumulated_score
                
        
    
    def hold_dice(self, dice : List[Dice]):
        if self._can_roll:
            raise GameError("You have to roll the dice before you can hold any of them!")


        if not isinstance(dice,list):
            raise GameError("You have to give a list of dice to hold")

        if len(dice) == 0:
            raise GameError("You have to hold back at least one die!")

        if len(dice) != len(set(dice)):
            raise GameError("You can't hold back the same dice multiple times!")
        
        for d in dice:
            if not isinstance(d, Dice):
                raise GameError("You have to put dice in the hold list")
            if not d.id in self._ids:
                raise GameError("That's not one of the dice we gave rolled, cheater cheater")
            if d in self._held:
                raise GameError("Hey, you already held that dice last time, no cheating!")

        self._turn_score += Turn.calc_score(dice)

        self._scored_on_last = True
        
        for d in dice:
            self._held.add(d)

        ## if we have scored on all the dice, they can roll again
        if len(self._held) == 6:
            self._held.clear

        for d in self._dice:
            if d not in self._held:
                d._unlock

        
        self._can_roll = True
        

    def is_straight(dice : List[Dice]):
        if len(dice) != 6:
            return False

        lst = list(dice)

        lst.sort(key=lambda x: x.current_value)

        return Turn.straight == [x.current_value for x in lst]


    def get_triples(dice : List[Dice]):
        dc = list(dice)
        dc.sort(key=lambda x: x.current_value)
        triples = []
        for ky, group in itertools.groupby(dc,lambda x: x.current_value):
            grp_lst = list(group)
            if len(grp_lst) == 6:
                triples.extend(grp_lst)
            elif len(grp_lst) >= 3:
                triples.extend(grp_lst[:3])

        return triples

    def get_ones(dice: List[Dice]):
        return [d for d in dice if d.current_value == 1]

    def get_fives(dice: List[Dice]):
        return [d for d in dice if d.current_value == 5]
    
