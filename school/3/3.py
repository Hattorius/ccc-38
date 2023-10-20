with open("level3_1.in") as f:
    lines = f.readlines()
    
lines = lines[1:]
seen = []
    
for line in lines:
    line = line.replace("\n", "")
    keys = [key.split(",") for key in line.split(" ")]
    seen.append(keys)
    
for i in range(len(seen)):
    for j in range(len(seen[i])):
        piece = seen[i][j]
        
        if i - 1 >= 0:
            abovePiece = seen[i - 1][j]
            if abovePiece[2] == "K" and piece[0] in "KE":
                seen[i][j][0] = "H"
            elif abovePiece[2] == "H" and piece[0] in "HE":
                seen[i][j][0] = "K"
        
        if j - 1 >= 0:
            leftPiece = seen[i][j - 1]
            if leftPiece[1] == "K" and piece[3] in "KE":
                seen[i][j][3] = "H"
            elif leftPiece[1] == "H" and piece[3] in "HE":
                seen[i][j][3] = "K"
                
        if i + 1 < len(seen):
            belowPiece = seen[i + 1][j]
            if belowPiece[0] == "K" and piece[2] in "KE":
                seen[i][j][2] = "H"
            elif belowPiece[0] == "H" and piece[2] in "HE":
                seen[i][j][2] = "K"
        
        if j + 1 < len(seen[i]):
            rightPiece = seen[i][j + 1]
            if rightPiece[3] == "K" and piece[1] in "KE":
                seen[i][j][1] = "H"
            elif rightPiece[3] == "H" and piece[1] in "HE":
                seen[i][j][1] = "K"
                
with open("level3_1.out", "w") as f:
    for line in seen:
        a = " ".join([",".join(piece) for piece in line])
        f.write(a + "\n")