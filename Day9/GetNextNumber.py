class row:
    def __init__(self, orig:[], missValue:int):
        self.orig = orig
        self.missValue = missValue

def parseLineToObj(line):
    tmp = line.strip().replace('\n', '').split(' ')
    tmp = [int(x) for x in tmp]
    return row(tmp, 0)

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day9/input.txt")
rows = []
for line in lines:
    r = parseLineToObj(line)
    rows.append(r)

def generateNextRow(r:row):
    nextRow = row([], 0)
    for i in range(len(r.orig)-1):
        nextRow.orig.append(r.orig[i+1] - r.orig[i])
    return nextRow
#print(f'row {rows[133].orig} - last value {rows[0].missValue}')
def findMissingBehindValue(r:row):
    if all(x == r.orig[0] for x in r.orig):
        r.missValue = r.orig[0]
        #print(f'row {r.orig} - last value {r.missValue}')
        return r.missValue
    else:
        nextRow = generateNextRow(r)
        nextRow.missValue = findMissingBehindValue(nextRow)
        #print(f'row {nextRow.orig} - last value {nextRow.missValue}')
        return r.orig[-1] + nextRow.missValue
    
def findMissingFrontValue(r:row):
    if all(x == r.orig[0] for x in r.orig):
        r.missValue = r.orig[0]
        return r.missValue
    else:
        nextRow = generateNextRow(r)
        nextRow.missValue = findMissingFrontValue(nextRow)
        return r.orig[0] - nextRow.missValue
#part 1
sum1 = 0
for ro in rows:
    sum1 += findMissingBehindValue(ro)
print(sum1)

#part 2
sum2 = 0
for ro in rows:
    sum2 += findMissingFrontValue(ro)
print(sum2)