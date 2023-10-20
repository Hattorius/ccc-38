import time
fileLevel = "5"

with open(f"level6_{fileLevel}.in") as f:
    lines = [line.strip() for line in f.readlines()]
    
mapSize = int(lines[0])
map = lines[1:mapSize + 1]
spots = [spots for spots in lines[mapSize + 2:]]

def findFullIsland(spotX, spotY):
    dimensions = [[1,0],[-1,0],[0,1],[0,-1]]
    seen = [[spotX, spotY]]
    
    while True:
        c = len(seen)
        
        for spot in seen:
            for dim in dimensions:
                nSpotX = spot[0] + dim[0]
                nSpotY = spot[1] + dim[1]
                
                if [nSpotX, nSpotY] not in seen and map[nSpotY][nSpotX] == "L":
                    seen.append([nSpotX, nSpotY])
                    
        if len(seen) == c:
            break
        
    return seen

def findIslandSpotsToGo(fullIsland):
    lowestX = [99999, 0]
    lowestY = [0, 99999]
    highestX = [0, 0]
    highestY = [0, 0]
    
    for point in fullIsland:
        if point[0] < lowestX[0]:
            lowestX = point
        if point[0] > highestX[0]:
            highestX = point
        if point[1] < lowestY[1]:
            lowestY = point
        if point[1] > highestY[1]:
            highestY = point
            
    return [[lowestY[0], lowestY[1] - 1], [highestX[0] + 1, highestX[1]], [highestY[0], highestY[1] + 1], [lowestX[0] - 1, lowestX[1]]]

def exists(a, b):
    try:
        map[a][b]
        return True
    except:
        return False

def showBoard(board, currentY, currentX, targetY, targetX):
    return
    print("")
    time.sleep(0.1)
    for y in range(len(board)):
        newX = []
        for x in range(len(board[y])):
            if y == currentY and x == currentX:
                newX.append("⛵")
            elif y == targetY and x == targetX:
                newX.append("❌")
            elif board[y][x] == "L":
                newX.append("🟨")
            else:
                newX.append("🟦")
            
        print("".join(newX))

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

def findBeginningSpot(fullIsland):
    lowestPos = [0,0]
    lowest = 9999999
    for pos in fullIsland:
        if sum(pos) < lowest:
            lowest = sum(pos)
            lowestPos = pos
            
    if map[lowestPos[1] - 1][lowestPos[0] - 1] == "W":
        return [lowestPos[0] - 1, lowestPos[1] - 1]
    elif map[lowestPos[1] - 1][lowestPos[0]] == "W":
        return [lowestPos[0], lowestPos[1] - 1]
    elif map[lowestPos[1]][lowestPos[0] - 1] == "W":
        return [lowestPos[0] - 1, lowestPos[1]]

results = []

for spot in spots:
    spot = [int(a) for a in spot.split(",")]
    fullIsland = findFullIsland(spot[0], spot[1])
    beginningSpot = findBeginningSpot(fullIsland)
    POI = findIslandSpotsToGo(fullIsland)
    # POI.append(beginningSpot)
    
    currentSpot = [POI[0][0], POI[0][1]]
    POI.append(POI[0])
    POI = POI[1:]
    
    fullPath = f"{currentSpot[0]},{currentSpot[1]} "
    for poi in POI:
        showBoard(map, currentSpot[1], currentSpot[0], poi[1], poi[0])
        path = pathFinding(currentSpot[1], currentSpot[0], map, poi[1], poi[0])
        
        for step in path["steps"]:
            if step == "U":
                currentSpot[1] -= 1
            elif step == "R":
                currentSpot[0] += 1
            elif step == "D":
                currentSpot[1] += 1
            elif step == "L":
                currentSpot[0] -= 1
            elif step == "DR":
                currentSpot[1] += 1
                currentSpot[0] += 1
            elif step == "DL":
                currentSpot[1] += 1
                currentSpot[0] -= 1
            elif step == "UR":
                currentSpot[1] -= 1
                currentSpot[0] += 1
            elif step == "UL":
                currentSpot[1] -= 1
                currentSpot[0] -= 1
                
            fullPath += f"{currentSpot[0]},{currentSpot[1]} "
            showBoard(map, currentSpot[1], currentSpot[0], poi[1], poi[0])
    
    results.append(" ".join(fullPath.split(" ")[:-2]))

with open(f"level6_{fileLevel}.out", "w") as f:
    for result in results:
        f.write(result + "\n")