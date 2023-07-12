# import Helper as MoveGenerator
import MoveGenerator
import sys
import FileInput

def minmaxGame(boardPosition, depth, resultantPosition,maximizingLevel):
    if(depth == 0):
        MoveGenerator.positionEvaluated +=1
        return MoveGenerator.staticEstimationMidgameEndgame(boardPosition), boardPosition
     
    if(maximizingLevel):
        maxValue = -sys.maxsize -1
        positions = MoveGenerator.generateMovesMidgameEndgame(boardPosition)
    else:
        maxValue = sys.maxsize
        positions = MoveGenerator.generateMovesMidgameEndgameBlack(boardPosition)

    for pos in positions:
        if(maximizingLevel):
             whiteMinMax = minmaxGame(pos, depth-1, resultantPosition,  False)
             if(whiteMinMax[0] > maxValue):
                 maxValue = whiteMinMax[0]
                 resultantPosition = pos
        else:
            blackMaxMin = minmaxGame(pos, depth-1, resultantPosition, True)
            if(blackMaxMin[0]  < maxValue):
                maxValue = blackMaxMin[0]
                resultantPosition = blackMaxMin[1]

    return maxValue , resultantPosition

 

if __name__ == "__main__":
    inputBoardFile = FileInput.readInputFile(sys.argv[1])
    outputBoardFile = sys.argv[2]
    depth = int(sys.argv[3])

    output = []
    resultantPosition = []
   

    output = minmaxGame(inputBoardFile, depth, resultantPosition, True)
    finalPos = ''.join(output[1])
    print('Board Position :' , finalPos)
    print('Positions evaluated by Static Estimation :', MoveGenerator.positionEvaluated)
    print('MINIMAX estimate :', output[0])
    
    
    FileInput.writeOutput(outputBoardFile, finalPos )
