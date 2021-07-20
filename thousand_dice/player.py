from typing import Optional, List
import itertools
from .turn import Turn

class Player:
    
    def __init__(self, name: str):
        self._name: str = name
        self._score: int = 0

    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score

    def play(self,turn : Turn):
        pass
