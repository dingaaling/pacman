# Python 3 - PAC-MAN Game
# Jennifer Ding

import sys
import numpy as np
from gameFunctions import *

# Read input-file.txt for game intializations: board dim, starting position, moves, and walls
def main():

    args = sys.argv
    fileName = str(args[1])

    inputVal = []
    for line in open(fileName):
        line = line.strip().split(' ')
        inputVal.append(line)

    # Check and load game intializations
    if (checkInput(inputVal) == True):

        boardDim, startPos = np.asarray(inputVal[0], dtype=int), np.asarray(inputVal[1], dtype=int)
        moves, walls = inputVal[2], np.asarray(inputVal[3:], dtype=int)

        # Check dimensions of input and then play and save game to game-file.txt
        if (checkDim(boardDim, startPos, moves, walls)==True):
            playGame(boardDim, startPos, moves, walls)
        else:
            print("Game Over")
    else:
        print("Game Over")


main()
