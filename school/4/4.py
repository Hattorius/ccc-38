with open("level4_example.in") as f:
    lines = f.readlines()

numPieces = int(lines[0])
pieces = [line.strip() for line in lines[1:numPieces + 1]]
board = lines[numPieces + 2:]

def e(i, j):
    try:
        return board[i][j]
    except:
        return False

for i in range(len(board)):
    for j in range(len(board[i])):
        char = board[i][j]
        
        rightChar = None
        leftChar = None
        
        topPiece = None
        rightPiece = None
        bottomPiece = None
        leftPiece = None
        
        if e(i, j+1):
            rightChar = board[i][j + 1]
        if e(i, j-1):
            leftChar = board[i][j - 1]
            
        if e(i-1, j):
            if 
            topPiece = board[i - 1][j]