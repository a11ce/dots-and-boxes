from common import *

import dotsAndBoxes

import random
import copy

def main():
    testGame = dotsAndBoxes.GameState(4)
    
    curPlayer = 1
    for _ in range(24):
            
        poss = testGame.possibleMoves()
        choice = random.choice(poss)
        madeBox = testGame.applyMove(choice[0],choice[1],curPlayer)
        if not madeBox:
            curPlayer = int(not curPlayer)
        testGame.printBoard()
        print(testGame.boardScore())
        print(testGame.possibleMoves())
        #input()
            
    
    print("SHOULD NOT contain X")
    testGame = dotsAndBoxes.GameState(2)
    testGame.applyMove(1,Point(0,0))
    testGame.applyMove(1,Point(0,1))
    testGame.applyMove(0,Point(0,0))
    testGame.printBoard()
    
    print("SHOULD NOT contain X and two boards should be different")
    testGame = dotsAndBoxes.GameState(3)
    testGame.applyMove(0, Point(2,1))
    testGame.applyMove(0, Point(1,1))
    testGame.applyMove(1, Point(1,2))
    testGame.applyMove(1, Point(1,0))
    
    testTwo = copy.deepcopy(testGame)
    testTwo.applyMove(0, Point(0,1))
    testTwo.printBoard()
    print("////")
    testGame.printBoard()
    
    testGame = dotsAndBoxes.GameState(4)
    testGame.applyMove(1, Point(0,1))
    testGame.applyMove(1, Point(0,2))
    testGame.applyMove(0, Point(2,2))
    testGame.applyMove(0, Point(2,1))
    testGame.applyMove(0, Point(2,0))
    testGame.applyMove(1, Point(1,0))
    testGame.applyMove(1, Point(1,3))
    testGame.printBoard()

if __name__ == "__main__":
    main()