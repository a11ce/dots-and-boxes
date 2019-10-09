import collections
import random
import copy

DirecLinks = collections.namedtuple("Links", "horz vert")
Point = collections.namedtuple("Point", "x y")

class GameState:
    def __init__(self, size):
        #size = size -1
        self.boardSize = size 
        self.links = DirecLinks(   
                [[False for i in range(size-1)] for j in range(size)],
                [[False for i in range(size)] for j in range(size-1)]
                )
                
        self.boxes = [[0 for i in range(size-1)] for j in range(size-1)]
        
    def applyMove(self, ori, idx):
        #print("MOVE: " + str(ori)  +" "+ str(idx))
        if self.links[ori][idx.x][idx.y]:
            raise Exception("Illegal move")
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
                        self.boxes[idx.x][idx.y] = True
                else:
                    if(
                        self.links[1-ori][idx.x-1][idx.y] and
                        self.links[1-ori][idx.x-1][idx.y+1] 
                    ):
                        print("owo")
                        self.boxes[idx.x-1][idx.y] = True
            else:
                if checkDir == 1:
                    if(
                        self.links[1-ori][idx.x][idx.y] and
                        self.links[1-ori][idx.x+1][idx.y]
                    ):
                        print("owo")
                        self.boxes[idx.x][idx.y] = True
                else:
                    if(
                        self.links[1-ori][idx.x][idx.y-1] and
                        self.links[1-ori][idx.x+1][idx.y-1]
                    ):
                        print("owo")
                        self.boxes[idx.x][idx.y-1] = True
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
                        print("X " if self.boxes[n][i] else "  ", end = "")
                    except:
                        pass
            except:
                pass
            print()
        
def possibleMoves(game):
    possMoves = []
    for link in gameState.links:
        if not link.isSet:
            possMoves.append(link)

if __name__ == "__main__":
    testGame = GameState(3)

    for _ in range(8):
        try:
            testGame.applyMove(random.randint(0,1), Point(random.randint(0,2),random.randint(0,2)))
        except:
            pass


    testGame.printBoard()

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