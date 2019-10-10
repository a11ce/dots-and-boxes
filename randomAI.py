from common import *

import random

class RandomAI:
    def nextMove(self, game):
        poss = game.possibleMoves()
        choice = random.choice(poss)
        return choice