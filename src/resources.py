# Class to abstract getting resources from the res folder

# Dictionary of resources
resources = {
    'pawn-white' : '../res/pieces/pawn-white.txt',
    'rook-white' : '../res/pieces/rook-white.txt',
    'bishop-white' : '../res/pieces/bishop-white.txt',
    'knight-white' : '../res/pieces/knight-white.txt',
    'queen-white' : '../res/pieces/queen-white.txt',
    'king-white' : '../res/pieces/king-white.txt',
    'pawn-black' : '../res/pieces/pawn-black.txt',
    'rook-black' : '../res/pieces/rook-black.txt',
    'bishop-black' : '../res/pieces/bishop-black.txt',
    'knight-black' : '../res/pieces/knight-black.txt',
    'queen-black' : '../res/pieces/queen-black.txt',
    'king-black' : '../res/pieces/king-black.txt',
    'board' : '../res/board.txt',
    'title' : '../res/title-chess.txt',
    'instructions' : '../res/instructions.txt'
}

# Get the resource
def getResource(resourceName):
    returnStr = ""
    with open(resources[resourceName], 'r') as f:
        returnStr = f.read()

    return returnStr
