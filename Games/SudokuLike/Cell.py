from typing import List
from Shape import Shape

class Cell:
    def __init__(self, val:int, possibleVals:set, inShapes:list):
        self.val:int = val
        self.possibleVals:set = possibleVals
        self.inShapes:List[Shape] = inShapes


