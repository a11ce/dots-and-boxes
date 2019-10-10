from common import *

import collections
import random
import copy

DirecLinks = collections.namedtuple("Links", "horz vert")


class GameState:
    def __init__(self, size):
        #size = size -1
        self.boardSize = size 
        self.links = DirecLinks(   
                [[False for i in range(size-1)] for j in range(size)],
                [[False for i in range(size)] for j in range(size-1)]
                )
                
        self.boxes = [[-1 for i in range(size-1)] for j in range(size-1)]
        
    def applyMove(self, ori, idx, whichPlayer=1):
        #print(str(whichPlayer) + " To Move")
        moveAgain = False
        #print("MOVE: " + str(ori)  +" "+ str(idx))
        
        if self.links[ori][idx.x][idx.y]:
            raise MoveException("Illegal move")
        if not (whichPlayer == 0 or whichPlayer == 1):
            raise Exception("Invalid player number")
        self.links[ori][idx.x][idx.y] = True
        # horz
        checkDirs = []
        oriY = ori == 1
        try:
            if (
                (oriY     and self.links[ori][idx.x][idx.y-1] and idx.y != 0)
                or
                (not oriY and self.links[ori][idx.x-1][idx.y] and idx.x != 0)
                ):
                checkDirs.append(-1)
        except:
            pass
        try:
            if (
                (oriY     and self.links[ori][idx.x][idx.y+1])
                or
                (not oriY and self.links[ori][idx.x+1][idx.y])
                ):
                checkDirs.append(1)     
        except:
            pass

        #print(checkDirs)
        for checkDir in checkDirs:
            if ori == 0:
                if checkDir == 1:
                    if(
                        self.links[1-ori][idx.x][idx.y] and
                        self.links[1-ori][idx.x][idx.y+1]
                    ):
                        print("owo")
                        self.boxes[idx.x][idx.y] = whichPlayer
                        moveAgain = True
                else:
                    if(
                        self.links[1-ori][idx.x-1][idx.y] and
                        self.links[1-ori][idx.x-1][idx.y+1] 
                    ):
                        print("owo")
                        self.boxes[idx.x-1][idx.y] = whichPlayer
                        moveAgain = True
            else:
                if checkDir == 1:
                    if(
                        self.links[1-ori][idx.x][idx.y] and
                        self.links[1-ori][idx.x+1][idx.y]
                    ):
                        print("owo")
                        self.boxes[idx.x][idx.y] = whichPlayer
                        moveAgain = True
                else:
                    if(
                        self.links[1-ori][idx.x][idx.y-1] and
                        self.links[1-ori][idx.x+1][idx.y-1]
                    ):
                        print("owo")
                        self.boxes[idx.x][idx.y-1] = whichPlayer
                        moveAgain = True
        return moveAgain
        
       # else:
    def printBoard(self):
        for n in range(self.boardSize):
            for link in self.links.horz[n]:
                print("* ", end = "")
                print( "- " if link else "  ", end = "")
            print("*")
            try:
                for i in range(len(self.links.vert[n])):
                    link = self.links.vert[n][i]
                    #print(i)
                    #print(n)
                    print( "| " if link else "  ", end = "")
                    try:
                        print("R " if self.boxes[n][i] == 0 else ("B " if self.boxes[n][i] == 1 else "  "), end = "")
                    except:
                        pass
            except:
                pass
            print()
        
    def possibleMoves(self):
        possMoves = []
        for ori in range(len(self.links)):
            
            for x in range(len(self.links[ori])):
                for y in range(len(self.links[ori][x])):
                    #if link == False:
                    #print(ori)
                    if self.links[ori][x][y] == False:
                        possMoves.append((ori,Point(x,y)))
        return possMoves
    def boardScore(self):
        sum = 0
        for row in self.boxes:
            for box in row:
                sum += (1 if box==1 else (-1 if box==0 else 0))
        return sum
        
if __name__ == "__main__":
    testGame = GameState(4)

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
    testGame = GameState(2)
    testGame.applyMove(1,Point(0,0))
    testGame.applyMove(1,Point(0,1))
    testGame.applyMove(0,Point(0,0))
    testGame.printBoard()

    print("SHOULD NOT contain X and two boards should be different")
    testGame = GameState(3)
    testGame.applyMove(0, Point(2,1))
    testGame.applyMove(0, Point(1,1))
    testGame.applyMove(1, Point(1,2))
    testGame.applyMove(1, Point(1,0))

    testTwo = copy.deepcopy(testGame)
    testTwo.applyMove(0, Point(0,1))
    testTwo.printBoard()
    print("////")
    testGame.printBoard()

    testGame = GameState(4)
    testGame.applyMove(1, Point(0,1))
    testGame.applyMove(1, Point(0,2))
    testGame.applyMove(0, Point(2,2))
    testGame.applyMove(0, Point(2,1))
    testGame.applyMove(0, Point(2,0))
    testGame.applyMove(1, Point(1,0))
    testGame.applyMove(1, Point(1,3))
    testGame.printBoard()