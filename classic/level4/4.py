fileLevel = "5"

with open(f"level4_{fileLevel}.in") as f:
    lines = [line.strip() for line in f.readlines()]
    
mapSize = int(lines[0])
map = lines[1:mapSize + 1]
spots = [spots.split(" ") for spots in lines[mapSize + 2:]]

def exists(a, b):
    try:
        map[a][b]
        return True
    except:
        return False
    
results = []

def pathFinding(startY, startX, board, targetY, targetX):
    steps = []
    seen = []
    neighbours = [ [-1,0,"U"], [1,0,"D"], [0,-1,"L"], [0,1,"R"], [1,1,"DR"], [1,-1,"DL"], [-1,1,"UR"], [-1,-1,"UL"] ]
    
    for n in neighbours:
        newY = startY + n[0]
        newX = startX + n[1]
        step = n[2]

        if exists(newY, newX) and board[newY][newX] == "W":
            g = {
                "steps": [step],
                "Y": newY,
                "X": newX
            }

            steps.append(g)
            if newY == targetY and newX == targetX:
                return g

            seen.append(str(newY) + "," + str(newX))
    
    while True:
        tempSteps = []
        for step in steps:
            for n in neighbours:
                newY = step["Y"] + n[0]
                newX = step["X"] + n[1]
                stepHuh = n[2]

                sstep = str(newY) + "," + str(newX)
                if exists(newY, newX) and board[newY][newX] == "W" and sstep not in seen:
                    g = {
                        "steps": step["steps"] + [stepHuh],
                        "Y": newY,
                        "X": newX
                    }

                    tempSteps.append(g)
                    seen.append(sstep)

                    if newY == targetY and newX == targetX:
                        return g

        steps = tempSteps

with open(f"level4_{fileLevel}.out", "w") as f:
    for spot in spots:
        spotA = [int(a) for a in spot[0].split(",")]
        spotB = [int(a) for a in spot[1].split(",")]
        
        if spotA == spotB:
            results.append(f"{spot[0]} {spot[1]}")
            continue
        
        path = pathFinding(spotA[1], spotA[0], map, spotB[1], spotB[0])
        coords = str(spotA[0]) + "," + str(spotA[1])
        for step in path["steps"]:
            if step == "U":
                spotA[1] -= 1
            elif step == "R":
                spotA[0] += 1
            elif step == "D":
                spotA[1] += 1
            elif step == "L":
                spotA[0] -= 1
            elif step == "DR":
                spotA[1] += 1
                spotA[0] += 1
            elif step == "DL":
                spotA[1] += 1
                spotA[0] -= 1
            elif step == "UR":
                spotA[1] -= 1
                spotA[0] += 1
            elif step == "UL":
                spotA[1] -= 1
                spotA[0] -= 1
            
            coords += " " + str(spotA[0]) + "," + str(spotA[1])
            
        f.write(coords + "\n")