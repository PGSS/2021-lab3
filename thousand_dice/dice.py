import random
import uuid
from .game_error import GameError

class Dice:

    def __init__(self):
        self._current_value: int = None
        self._id = uuid.uuid4()
        self._is_locked = False

    @property
    def current_value(self):
        return self._current_value

    @property
    def id(self):
        return self._id

    @property
    def is_locked(self):
        return self._is_locked

    def roll(self):
        if self._is_locked:
            raise GameError("You can't roll this die, you're holding on to it!")

        self._current_value = random.randint(1, 6)

    def _lock(self):
        self._is_locked = True

    def _unlock(self):
        self._is_locked = False

    def __hash__(self):
        return self.id.__hash__()
        
    def __eq__(self,other):
        if isinstance(other, Dice):
            return self.id == other.id
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.current_value)
