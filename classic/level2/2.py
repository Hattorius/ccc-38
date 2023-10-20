fileLevel = "5"

with open(f"level2_{fileLevel}.in") as f:
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

for spot in spots:
    spotA = [int(a) for a in spot[0].split(",")]
    spotB = [int(a) for a in spot[1].split(",")]
    
    if spotA == spotB:
        results.append("SAME")
        continue
    
    paths = [spotA.copy()]
    seen = [spotA.copy()]
    found = False
    while not found:
        newPaths = []
        dimensions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for path in paths:
            for dimension in dimensions:
                if exists(path[1] + dimension[1], path[0] + dimension[0]):
                    newPathA = path[0] + dimension[0]
                    newPathB = path[1] + dimension[1]
                    
                    if map[newPathB][newPathA] == "L" and [newPathA, newPathB] not in seen:
                        if spotB == [newPathA, newPathB]:
                            found = True
                            results.append("SAME")
                            break
                        
                        seen.append([newPathA, newPathB])
                        newPaths.append([newPathA, newPathB])
                        
            if found:
                break
        
        if not found:
            paths = newPaths.copy()
            
            if len(paths) == 0:
                results.append("DIFFERENT")
                break
            
with open(f"level2_{fileLevel}.out", "w") as f:
    for result in results:
        f.write(result + "\n")