import MoveGenerator
import sys
import FileInput

def abGame(boardPosition, depth, resultantPosition,maximizingLevel , alpha , beta):
    if(maximizingLevel):
        maxValue = alpha
        positions = MoveGenerator.generateMovesMidgameEndgame(boardPosition)
    else:
        maxValue = beta
        positions = MoveGenerator.generateMovesMidgameEndgameBlack(boardPosition)
    
    if(depth == 0):
        MoveGenerator.positionEvaluated +=1
        return MoveGenerator.staticEstimationMidgameEndgame(boardPosition), boardPosition

    for pos in positions:
        if(alpha >= beta):
            break
        if(maximizingLevel):
             whiteMinMax = abGame(pos, depth-1, resultantPosition,  False , alpha , beta)
             alpha = max(maxValue , alpha)
             if(whiteMinMax[0] > alpha):
                maxValue = whiteMinMax[0]
                resultantPosition = pos
        else:
            blackMaxMin = abGame(pos, depth-1, resultantPosition, True, alpha, beta)
            beta = min(maxValue, beta)
            if(blackMaxMin[0]  < beta):
                maxValue = blackMaxMin[0]
                resultantPosition = blackMaxMin[1]
        

    return maxValue , resultantPosition


if __name__ == "__main__":
    inputBoardFile = FileInput.readInputFile(sys.argv[1])
    outputBoardFile = sys.argv[2]
    depth = int(sys.argv[3])

    output = []
    resultantPosition = []
    output = abGame(inputBoardFile, depth, resultantPosition, True , -sys.maxsize-1, sys.maxsize)
    finalPos = ''.join(output[1])
    print('Board Position :' , finalPos)
    print('Positions evaluated by Static Estimation :', MoveGenerator.positionEvaluated)
    print('MINIMAX estimate :', output[0])
    FileInput.writeOutput(outputBoardFile, finalPos)
