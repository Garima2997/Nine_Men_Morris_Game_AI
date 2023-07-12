positionEvaluated = 0

# to generate and add new position
def generateAdd(position):
    newPositions = []
    for i in range(len(position)):
        if (position[i] == 'x'):
            copyOfPositions = position.copy()
            copyOfPositions[i] = 'W'
            if (closeMill(i, copyOfPositions)):
                generateRemove(copyOfPositions, newPositions)
            else:
                newPositions.append(copyOfPositions)
    return newPositions

# to determine close mill
def closeMill(location, position):
    pos = position[location]
    if (pos == 'x'):
        return False
    if (location == 0 and ((position[6] == pos and position[18] == pos ))):
        return True
    elif (location == 1 and ((position[11] == pos and position[20] == pos))):
        return True
    elif (location == 2 and ((position[7] == pos and position[15] == pos))):
        return True
    elif (location == 3 and ((position[10] == pos and position[17] == pos))):
        return True
    elif (location == 4 and (position[8] == pos and position[12] == pos)):
        return True
    elif (location == 5 and ((position[9] == pos and position[14] == pos)) ):
        return True    
    elif (location == 6 and ((position[7] == pos and position[8] == pos) or (position[0] == pos and position[18] == pos)) ):
        return True
    elif (location == 7 and ((position[6] == pos and position[8] == pos) or (position[2] == pos and position[15] == pos) )):
        return True
    elif (location == 8 and ((position[6] == pos and position[7] == pos) or (position[4] == pos and position[12] == pos)) ):
        return True
    elif (location == 9 and ((position[5] == pos and position[14] == pos) or (position[10] == pos and position[11] == pos) )):
        return True
    elif (location == 10 and ((position[3] == pos and position[17] == pos) or (position[9] == pos and position[11] == pos)) ):
        return True
    elif (location == 11 and( (position[1] == pos and position[20] == pos) or (position[9] == pos and position[10] == pos) )):
        return True 
    elif (location == 12 and ((position[4] == pos and position[8] == pos) or (position[13] == pos and position[14] == pos)) ):
        return True
    elif (location == 13 and ((position[12] == pos and position[14] == pos) or (position[16] == pos and position[19] == pos)) ):
        return True
    elif (location == 14 and ((position[5] == pos and position[9] == pos) or (position[12] == pos and position[13] == pos)) ):
        return True 
    elif (location == 15 and ((position[7] == pos and position[2] == pos) or (position[16] == pos and position[17] == pos)) ):
        return True
    elif (location == 16 and ((position[13] == pos and position[19] == pos) or (position[15] == pos and position[17] == pos)) ):
        return True    
    elif (location == 17 and ((position[3] == pos and position[10] == pos) or (position[15] == pos and position[16] == pos)) ):
        return True 
    elif (location == 18 and ((position[0] == pos and position[6] == pos) or (position[19] == pos and position[20] == pos)) ):
        return True
    elif (location == 19 and ((position[13] == pos and position[16] == pos) or (position[18] == pos and position[20] == pos) )):
        return True
    elif (location == 20 and ((position[1] == pos and position[11] == pos) or (position[18] == pos and position[19] == pos) )):
        return True
    else:
        return False

def generateRemove(boardPosition , newPosition):
    newListPos = newPosition.copy()
    for i in range(len(boardPosition)):
        copyBoardPosition = boardPosition.copy()
        if(boardPosition[i] == 'B'):
            if(not closeMill(i, boardPosition)):
                copyBoardPosition[i] = 'x'
                newListPos.append(copyBoardPosition)
            else:
                newListPos.append(copyBoardPosition)
    return newListPos

# fucntion to generate moves
def generateMove(boardPosition):
    newMovePositions = []
    for i in range(len(boardPosition)):
        if(boardPosition[i] == 'W'):
            neighborList = neighbor(i)
            for k in neighborList:
                if(boardPosition[k] == 'x'):
                    copyBoardPosition = boardPosition.copy()
                    copyBoardPosition[i] = 'x'
                    copyBoardPosition[k] = 'W'
                    if(closeMill(k, copyBoardPosition)):
                        generateRemove(copyBoardPosition,newMovePositions)
                    else:
                        newMovePositions.append(copyBoardPosition)
    return newMovePositions


# to check the neighbor input pieces in board
def neighbor(position):
    neighbor = []
    if position == 0:
        neighbor = [1 ,6]
    elif position == 1:
        neighbor = [0, 11]
    elif position == 2:
        neighbor = [3, 7]
    elif position == 3:
        neighbor = [2, 10]
    elif position == 4:
        neighbor = [5, 8]
    elif position == 5:
        neighbor = [4, 9]
    elif position == 6:
        neighbor = [0, 7, 18]
    elif position == 7:
        neighbor = [2, 6, 8, 15]
    elif position == 8:
        neighbor = [4, 7, 12]
    elif position == 9:
        neighbor = [5, 10, 14]
    elif position == 10:
        neighbor = [3, 9, 11, 17]
    elif position == 11:
        neighbor = [1, 10, 20]
    elif position == 12:
        neighbor = [8, 13]
    elif position == 13:
        neighbor = [12, 14, 16]
    elif position == 14:
        neighbor = [9, 13]
    elif position == 15:
        neighbor = [7, 16]
    elif position == 16:
        neighbor = [13, 15, 17, 19]
    elif position == 17:
        neighbor = [10, 16]
    elif position == 18:
        neighbor = [6, 19]
    elif position == 19:
        neighbor = [16, 18, 20]
    elif position == 20:
        neighbor = [11, 19]
    return neighbor

# to perform hopping 
def generateHopping(position):
    newHopPositions =[]
    for i in range(len(position)):
        if(position[i] =='W'):
            for k in range(len(position)):
                if(position[k] == 'x'):
                    copyBoardPosition = position.copy()
                    copyBoardPosition[i] = 'x'
                    copyBoardPosition[k] = 'W'
                    if(closeMill(k, copyBoardPosition)):
                        # generateRemove(copyBoardPosition, newHopPositions)
                        # when are we returning the list 
                        generateRemove(copyBoardPosition, newHopPositions)
                    else:
                        newHopPositions.append(copyBoardPosition)
    return newHopPositions

# generates moves in opening phase
def generateMovesOpening(position):
    return generateAdd(position)

# generate moves from black pieces in opening phase
def generateMovesOpeningBlack(position):
    boardPositionBlack = swap(position)
    blackPositions = generateAdd(boardPositionBlack)
    blackMoveList = []
    for pos in blackPositions:
        blackMoveList.append(swap(pos))
    return blackMoveList
    
# generates moves in midgame endgame phase
def generateMovesMidgameEndgame(position):
    count= 0
    for i in range(len(position)):
        if(position[i] == 'W'):
            count +=1
    if(count == 3):
        return generateHopping(position)
    else:
        return generateMove(position)

# generate moves from black pieces in midgame endgame phase
def generateMovesMidgameEndgameBlack(position):
    blackPositions = swap(position)
    blackMoves = generateMovesMidgameEndgame(blackPositions)
    blackMoveList = []
    for pos in blackMoves:
        blackMoveList.append(swap(pos))
    return blackMoveList

# static estimation function for midgame endgame
def staticEstimationMidgameEndgame(position):
    noOfWhitePieces = getPieceCount(position , 'W')
    noOfBlackPieces = getPieceCount(position , 'B')
    midgameEndgameBlackMove = generateMovesMidgameEndgameBlack(position)
    noOfBlackMoves = len(midgameEndgameBlackMove)

    if noOfBlackPieces <= 2:
        return 10000
    elif noOfWhitePieces <=2:
        return -10000
    elif noOfBlackMoves == 0:
        return 10000
    else:
        return ( (1000*(noOfWhitePieces - noOfBlackPieces)) - noOfBlackMoves)

# static estimation function for opening
def staticEstimationOpening(position):
    noOfWhitePieces = getPieceCount(position, 'W')
    noOfBlackPieces = getPieceCount(position, 'B')
    return (noOfWhitePieces - noOfBlackPieces)

# IMPROVED static estimation function for opening phase
def staticEstimationOpeningImproved(position):
    noOfWhitePieces = getPieceCount(position, 'W')
    noOfBlackPieces = getPieceCount(position, 'B')
    whiteMove = generateMove(position)
    noOfWhiteMoves = len(whiteMove)
    return 2*(noOfWhiteMoves + noOfWhitePieces) - noOfBlackPieces

# function to count the no of black and white peices in the board
def getPieceCount(pos, type):
    count =0
    for i in pos:
        if(i == type):
            count +=1
    return count

# function to swap the board for playing as black
def swap(boardPosition):
    swapBoardPosition = []
    for i in boardPosition:
        if i == 'W':
            swapBoardPosition.append('B')
        elif i == 'B':
            swapBoardPosition.append('W')
        else:
            swapBoardPosition.append('x')
    return swapBoardPosition

# IMPROVED static estimation function for midgame endgame phase
def staticEstimationMidgameEndgameImproved(position):
    noOfWhitePieces = getPieceCount(position , 'W')
    noOfBlackPieces = getPieceCount(position , 'B')
    midgameEndgameWhiteMove = generateMovesMidgameEndgame(position)
    midgameEndgameBlackMove = generateMovesMidgameEndgameBlack(position)
    noOfBlackMoves = len(midgameEndgameBlackMove)
    noOfWhiteMoves = len(midgameEndgameWhiteMove)

    if noOfBlackPieces <= 2:
        return 10000
    elif noOfWhitePieces <=2:
        return -10000
    elif noOfBlackMoves == 0:
        return 10000
    else:
        return 1000*(noOfWhiteMoves) - (noOfBlackMoves )
    