def readInputFile(inputFile):
    with open(inputFile, 'r') as f:
        boardPos = f.read()
    return list(boardPos)

def writeOutput(outputFileName, finalPosition):

    
 
    with open(outputFileName, 'w') as f:
        f.writelines(finalPosition)