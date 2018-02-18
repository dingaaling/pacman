import sys
import numpy as np

# Visualize board positions: 1   - Positions with Coins | 0   - Starting Point | Nan - Walls
def createBoard(boardDim, pos, walls):
    board = np.ones((boardDim[0], boardDim[1]))
    board[pos[0], pos[1]] = 0

    for wall in walls:
        board[wall[0], wall[1]] = np.nan

    return board

# Flip Numpy r,c oriented board to Cartesian x,y oriented board
def flipBoard(board):
    finalBoard = np.rot90(board)
    return finalBoard

# Dictionary of possible positions; walls are excluded because they are not available positions
# Starting point is denoted by 0; Other points are given 1 to denote available token. This is updated to 0 when Pacman moves onto the point, collecting the coin
def makeBoardDict(board):
    boardDict = {}

    # Encode starting point - 0
    coord = np.argwhere(board==0)
    boardDict[str(coord[0])] = 0

    # Encode points with coins - 1
    coords = np.argwhere(board==1)
    for coord in coords:
        boardDict[str(coord)] = 1

    return boardDict

# Convert moves from cardinal directions to positions in the grid. Movements oriented for Numpy r,c array
def convertMoves(moves):
    moves = ''.join(moves)
    moveList = []
    for move in moves:
        if move == "N":
            moveList.append([0, 1])
        elif move == "S":
            moveList.append([0, -1])
        elif move == "E":
            moveList.append([1, 0])
        elif move == "W":
            moveList.append([-1, 0])

    return moveList

# Check moves in boardDict to update Position and Coin count
def makeMoves(startPos, moveList, boardDict):
    pos = startPos
    coinCount = 0

    for move in moveList:
        origPos = pos
        pos = np.add(pos, move)

        if(str(pos) in boardDict):
            coinCount+= boardDict[str(pos)]
            if (boardDict[str(pos)] == 1):
                boardDict[str(pos)] = 0
        else:
            pos = origPos
            # print(pos, "Not in Dict!")

    # Print final position at end of game and total coins collected
    print(pos[0], pos[1])
    print(coinCount)

    return pos

# Check the input file has the appropriate number of lines and kind of input for each line
def checkInput(inputVal):

    if len(inputVal) < 4:
        print("You're missing some inputs! Please check the input file.")
        return False

    acceptedMoves, inputMoves = "NESW", ''.join(inputVal[2])
    for move in inputMoves:
        if acceptedMoves.find(move) == -1:
            print("Wrong move directions detected: %s. Please give N E S W moves only." %(move))
            break
    else:
        return True

# Check the dimensions and position of board, starting point, and walls are valid
def checkDim(boardDim, startPos, moves, walls):

    # Check dimensions for numbers
    if not(boardDim.shape[0] == 2):
        print("Board Dimension %d is not a valid size. Please enter two numbers." %(boardDim.shape[0]))

    elif not(startPos.shape[0] == 2):
        print("Start Position %d is not a valid size. Please enter two numbers." %(startPos.shape[0]))

    elif not(walls.shape[1] ==2):
        print("Wall dimensions are not a valid size. Please enter two numbers for each wall.")

    # Starting Point not on the Board
    elif (startPos[0] >= boardDim[0]) or (startPos[1] >= boardDim[1]):
        print("Your starting point (%d,%d) is off the charts... literally." % (startPos[0], startPos[1]))
        print("Choose another starting point smaller than (%d,%d) or make a bigger board!" % (boardDim[0], boardDim[1]))

    # Starting Point on a Wall
    elif any(np.equal(walls,startPos).all(1)):
        print("Your starting point (%d,%d) is on a wall! Please choose another." % (startPos[0], startPos[1]))

    # Any Walls not on the Board
    elif (walls[:,0]>=boardDim[0]).any() or (walls[:,1]>=boardDim[1]).any():
        print("One of your walls isn't on the board. Choose another!")

    else:
        return True

# Play and save game
def playGame(boardDim, startPos, moves, walls):
    startBoard = createBoard(boardDim, startPos, walls)
    boardDict = makeBoardDict(startBoard)
    moveList = convertMoves(moves)
    finalPos = makeMoves(startPos, moveList, boardDict)
    finalBoard = createBoard(boardDim, finalPos, walls)

    # Write game moves to game-file
    gameFile = open("game-file.txt", "w", errors="ignore")
    gameFile.write("Starting Board\n")
    gameFile.write(str(flipBoard(startBoard)))
    gameFile.write("\n\nEnding Board\n")
    gameFile.write(str(flipBoard(finalBoard)))
    gameFile.close()
