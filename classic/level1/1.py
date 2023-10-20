with open("level1_5.in") as f:
    lines = [line.strip() for line in f.readlines()]
    
mapSize = int(lines[0])
map = lines[1:mapSize + 1]
spots = lines[mapSize + 2:]

with open("level1_5.out", "w") as f:
    for spot in spots:
        spot = [int(a) for a in spot.split(",")]
        value = map[spot[1]][spot[0]]
        f.write(value + "\n")