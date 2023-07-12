import MoveGenerator
import sys
import FileInput

def minmaxOpeningBlack(boardPosition, depth, resultantPosition,maximizingLevel):
    if(maximizingLevel):
        maxValue = -sys.maxsize -1
        positions = MoveGenerator.generateMovesOpeningBlack(boardPosition)
    else:
        maxValue = sys.maxsize
        positions = MoveGenerator.generateMovesOpening(boardPosition)
    
    if(depth == 0):
        MoveGenerator.positionEvaluated +=1
        return MoveGenerator.staticEstimationOpening(boardPosition), boardPosition

    for pos in positions:
        if(maximizingLevel):
             whiteMinMax = minmaxOpeningBlack(pos, depth-1, resultantPosition,  False)
             if(whiteMinMax[0] > maxValue):
                 maxValue = whiteMinMax[0]
                 resultantPosition = pos
        else:
            blackMaxMin = minmaxOpeningBlack(pos, depth-1, resultantPosition, True)
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
    output = minmaxOpeningBlack(inputBoardFile, depth, resultantPosition, True)
    finalPos = ''.join(output[1])
    print('Board Position :' , finalPos)
    print('Positions evaluated by Static Estimation :', MoveGenerator.positionEvaluated)
    print('MINIMAX estimate :', output[0])
    FileInput.writeOutput(outputBoardFile, finalPos )
