with open("level2_5.in") as f:
    lines = f.readlines()
    
lines = lines[1:]
seen = []

def turnForHighestNumber(bits):
    highest = bits
    highestNumber = 0
    for _ in range(4):
        number = int(bits, 2)
        if number > highestNumber:
            highestNumber = number
            highest = bits
            
        bits = bits[3] + bits[:-1]
        
    return highest

for line in lines:
    line = line.replace("\n", "")
    bit = ""
    for pos in [0, 2, 4, 6]:
        if line[pos] == "H":
            bit += "0"
        else:
            bit += "1"
    seen.append(turnForHighestNumber(bit))

result = []
seenValues = []
for value in seen:
    if value in seenValues:
        continue
    
    result.append([
        seen.count(value),
        ",".join([*value.replace("1", "K").replace("0", "H")])
    ])
    seenValues.append(value)

with open("level2_5.out", "w") as f:
    for value in result:
        f.write(str(value[0]) + " " + value[1] + "\n")