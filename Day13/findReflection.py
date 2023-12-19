from collections import Counter
def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day13/input.txt")
# Split lines by empty line
patterns = []
pattern = []

for i in range(len(lines)):
    if lines[i] == '\n' or i == len(lines)-1:
        patterns.append(pattern)
        pattern = []
        continue
    pattern.append(lines[i].strip())

def FindPotentialReflection(line: str, result: list):
    potentialMirrors = [] 
    for i in result:
        if i < len(line)/2:
            inFront = line[:i]
            behind = line[i+len(inFront)-1:i-1:-1]
        else:
            behind = line[i:]
            inFront = line[i-1:i-len(behind)-1:-1]
        if inFront == behind:
            potentialMirrors.append(i)
    return potentialMirrors

def getReflectionsHorizontalSearch(pattern: list[str]):
    startH = [i for i in range(1, len(pattern[0]))]
    for line in pattern:
        #print(f'cols that are reflective {startH}')
        startH = FindPotentialReflection(line, startH)
        if startH == []:
            print('No potential mirrors')
            break
    #print(f'cols that are reflective {startH}')
    return startH
#part 1
sum0 = 0
for pattern in patterns:
    #Horizontal
    startH = getReflectionsHorizontalSearch(pattern)
    # #vertical
    rotated_pattern = list(zip(*pattern[::1]))
    startV = getReflectionsHorizontalSearch(rotated_pattern)
    sum0 += sum(startH) + sum(startV * 100)
        
print (f'sum0: {sum0}')   

#part 2
def getpotentialMirrors(pattern: list[str]):
    startH = [i for i in range(1, len(pattern[0]))]
    potentialRowsForLines = []
    for line in pattern:
        potentialRows = FindPotentialReflection(line, startH)
        print(f'rows that are potentially reflective {potentialRows}')
        potentialRowsForLines.append(potentialRows)
        # Flatten the sublists and exclude items in horizLines
    filtered_rows = [row for sublist in potentialRowsForLines for row in sublist]
    # Count the occurrences of each item
    counts = Counter(filtered_rows)

    # Get the common item has quantity qual to len(pattern) -1
    most_common_items = [item for item in counts.items() if item[1] == len(pattern) -1]

    return most_common_items[0] if most_common_items != [] else (0,0)

sum1 = 0
for i in range(len(patterns)):
    #Horizontal
    hor = getpotentialMirrors(patterns[i])
    #vertical
    rotated_pattern = list(zip(*patterns[i][::1]))
    ver = getpotentialMirrors(rotated_pattern)

    print(f'pattern {i}, row: {len(patterns[i])}, col: {len(patterns[i][0])} hor: {hor}, ver: {ver}')
    sum1 += hor[0] + ver[0] * 100
        
print (f'sum1: {sum1}')   