with open("level1_5.in") as f:
    lines = f.readlines()
    
lines = lines[1:]
seen = {}

for line in lines:
    line = line.replace("\n", "")
    if line in seen:
        seen[line] += 1
    else:
        seen[line] = 1

with open("level1_5.out", "w") as f:
    for a in seen:
        f.write(str(seen[a]) + " " + a + "\n")