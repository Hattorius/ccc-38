fileLevel = "5"

with open(f"level3_{fileLevel}.in") as f:
    lines = [line.strip() for line in f.readlines()]
    
mapSize = int(lines[0])
spots = [spots.split(" ") for spots in lines[mapSize + 2:]]
results = []

def is_diagonal(previous, current):
    prev = [int(a) for a in previous.split(",")]
    curr = [int(a) for a in current.split(",")]
    
    diffA = abs(prev[0] - curr[0])
    diffB = abs(prev[1] - curr[1])
        
    return diffA == diffB

def getAdjacentCoords(coord):
    x, y = coord
    adjacent_coords = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return adjacent_coords

ii = 1
for route in spots:
    seen = []
    invalid = False
    
    for i in range(len(route)):
        previousSpot = route[i - 1] if i - 1 >= 0 else None
        spot = route[i]
        
        if spot in seen and not invalid:
            results.append("INVALID")
            invalid = True
            break
        
        if previousSpot is not None and is_diagonal(previousSpot, spot):
            prev = [int(a) for a in previousSpot.split(",")]
            curr = [int(a) for a in spot.split(",")]
            prevAdj = getAdjacentCoords(prev)
            currAdj = getAdjacentCoords(curr)
        
            adjacents = [value for value in prevAdj if value in currAdj]
        
            if ",".join([str(a) for a in adjacents[0]]) in seen and ",".join([str(a) for a in adjacents[1]]) in seen and not invalid:
                invalid = True
                results.append("INVALID")
                
        seen.append(spot)
        
    if not invalid:
        results.append("VALID")
        
    ii += 1
    
with open(f"level3_{fileLevel}.out", "w") as f:
    for result in results:
        f.write(result + "\n")