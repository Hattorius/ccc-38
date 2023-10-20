with open("level4_example.in") as f:
    lines = f.readlines()
    
numPieces = int(lines[0])
pieces = [word.split(",") for word in [line.strip() for line in lines[1:numPieces + 1]]]
print(pieces)
lines = lines[numPieces + 2:]
seen = []
   
def split_string_every_x(input_string, x):
    a = [input_string[i:i + x] for i in range(0, len(input_string), x)]
    
    for i in range(len(a)):
        if a[i][-1] == " ":
            a[i] = a[i][:-1]
        if a[i] == "       ":
            a[i] = ",,,"
        
    return a
    
for line in lines:
    line = line.replace("\n", "")
    line = split_string_every_x(line, 8)
    keys = [word.split(",") for word in line]
    seen.append(keys)
  
K = "K"
H = "H"
E = "E"

# Function to check if two pieces fit together
def pieces_fit(piece1, piece2):
    return piece1 != piece2

# Function to rotate a piece 90 degrees clockwise
def rotate_piece(piece):
    return list(zip(*piece[::-1]))

def if_exist(value, index):
    try:
        value[index]
        return True
    except:
        return False
    
def if_exists(value, x, y):
    try:
        value[x][y]
        return True
    except:
        return False

# Function to assemble the puzzle
def assemble_puzzle(puzzle, inner_pieces):
    n = len(puzzle)
    for piece in inner_pieces:
        for _ in range(4):
            # Rotate the piece
            rotated_piece = rotate_piece(piece)
            if if_exists(puzzle, 0, 1) and if_exist(rotate_piece, 0) and pieces_fit(puzzle[0][-1], rotated_piece[0]):
                # Place the piece in the puzzle
                puzzle[0].append(rotated_piece[0])
                for i in range(1, n):
                    if if_exists(puzzle, i, -1) and if_exist(rotated_piece, i) and pieces_fit(puzzle[i][-1], rotated_piece[i]):
                        puzzle[i].append(rotated_piece[i])
                    else:
                        break
                else:
                    break
                # Remove the last placed row if the piece didn't fit entirely
                puzzle[0].pop()
        else:
            print("No solution found.")
            return

    # Print the assembled puzzle
    for row in puzzle:
        print(" ".join(row))
        
assemble_puzzle(seen, pieces)