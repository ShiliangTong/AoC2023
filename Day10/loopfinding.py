class pipe:
    def __init__(self, x:int, y:int, value: chr):
        self.x = x
        self.y = y
        self.value = value

symbols = {
    '|': [True, False, True, False],  # north, east, south, west
    '-': [False, True, False, True],
    'L': [True, True, False, False],
    'J': [True, False, False, True],
    '7': [False, False, True, True],
    'F': [False, True, True, False]
}

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day10/input.txt")
pipeMap = []
loopDic = {}
loop = [] # list of pipe (x,y,s)
for i in range(len(lines)):
    r = list(lines[i].strip().replace('\n', ''))
    if 'S' in r:
        c = r.index('S')
        print("Index of 'S' in lines[{}]: {}".format(i, c))
        loop.append(pipe(i, c, 'S'))
        loopDic[f'{i},{c} loop len{len(loop)}'] = 'S'
    pipeMap.append(r)

loop.append(pipe(loop[-1].x+1, loop[-1].y, pipeMap[loop[-1].x+1][loop[-1].y]))
loopDic[f'{loop[-1].x},{loop[-1].y}'] = pipeMap[loop[-1].x][loop[-1].y]
print(f'{loop[-1].x},{loop[-1].y} loop len{len(loop)}-|')
# defficulty is a lot lower that only 1 route is possible
# I can only assume that there is no closed loop in the main loop
def findNextPipe(pi: pipe):
    prev = pipe(loop[-2].x, loop[-2].y, loop[-2].value)
    FromDirection = [prev.x<pi.x, prev.y>pi.y ,prev.x>pi.x, prev.y<pi.y]
    dir = [(a and not b) for a, b in zip(symbols[pi.value], FromDirection)]

    nextX = pi.x + (-1 if dir[0] else (1 if dir[2] else 0))
    nextY = pi.y + (-1 if dir[3] else (1 if dir[1] else 0))
    next = pipe(nextX, nextY, pipeMap[nextX][nextY])
    print(f'{next.x},{next.y}-{next.value}, loop len{len(loop)}')
    loop.append(next)
    loopDic[f'{next.x},{next.y}'] = next.value
    #print(f'next pipe is {next.value} at {next.x},{next.y}')

while loop[-1].value != 'S':
    findNextPipe(loop[-1])

print(f'loop len is {(len(loop)-2)/2}')

# Part 2
# create dict of all pipes, key is x,y, value is pipe.value
MapDic = {}
for i in range(len(pipeMap)):
    for j in range(len(pipeMap[i])):
        MapDic[f'{i},{j}'] = pipeMap[i][j]


#scan from four sides, and exclude all pipes that are not in the loop
excludedPipes = {}
for row in range(len(pipeMap)):
    for col in range(len(pipeMap[row])):
        if f'{row},{col}' in loopDic.keys():    
            break
        else:
            excludedPipes[f'{row},{col}'] = pipeMap[row][col]
            print(f'exclude {row},{col}, value is {pipeMap[row][col]}')
    for col in range(len(pipeMap[row])-1, 0, -1):
        if f'{row},{col}' in loopDic.keys():    
            break
        else:
            excludedPipes[f'{row},{col}'] = pipeMap[row][col]
            print(f'exclude {row},{col}, value is {pipeMap[row][col]}')
for col in range(len(pipeMap[0])):
    for row in range(len(pipeMap)):
        if f'{row},{col}' in loopDic.keys():    
            break
        else:
            excludedPipes[f'{row},{col}'] = pipeMap[row][col]
            print(f'exclude {row},{col}, value is {pipeMap[row][col]}')
    for row in range(len(pipeMap)-1, 0, -1):
        if f'{row},{col}' in loopDic.keys():    
            break
        else:
            excludedPipes[f'{row},{col}'] = pipeMap[row][col]
            print(f'exclude {row},{col}, value is {pipeMap[row][col]}')

# below is the tricky part to get the pipe surrounded by the loop
def getCellsInLoopForCurrentLine(row : int):
    cells = {cell for cell in loopDic if f'{row},' in cell.key}
    return cells

def isOneTimeCrossCorner(sym1: chr, sym2: chr):
    if sym1 == '|' or sym2 == '|':
        return False
    if sym1 == 'L' and (sym2 == '7' or sym2 == '-'):
        return True
    if sym1 == 'F' and (sym2 == 'J' or sym2 == '-'):
        return True

    return False
#excluding all pipes that are already scanned away, get the outer pipes if it is in the odd section that the loop passes thru the row
def getSectionsForCurrentLine(row: int):
    sections = []
    start = None
    end = None
    crossRowTimes = 0
    pipeCrossStart = ''
    for i in range(len(pipeMap[row])):
        if f'{row},{i}' not in loopDic.keys():
            if start is None:
                start = i
                pipeCrossStart = ''
        else: 
            if start is not None and end is None:
                end = i-1
                sections.append((start, end, crossRowTimes))
                print(f'row {row} section {start} to {end}, crossRowTimes is {crossRowTimes}')
                start = None
                end = None
                crossRowTimes += 1
                pipeCrossStart = loopDic[f'{row},{i}']
            elif not isOneTimeCrossCorner(pipeCrossStart, pipeMap[row][i]): # _|- count as 1 time cross
                pipeCrossStart = loopDic[f'{row},{i}']
                crossRowTimes += 1
    for i in range(len(sections)):
        if sections[i][2] % 2 == 0:
            for j in range(sections[i][0], sections[i][1]+1):
                if not f'{row},{j}' in excludedPipes.keys():
                    excludedPipes[f'{row},{j}'] = pipeMap[row][j]
                    print(f'exclude {row},{j}, value is {pipeMap[row][j]}')

for row in range(len(pipeMap)):
    getSectionsForCurrentLine(row)

total = len(pipeMap) * len(pipeMap[0])
print(f'total is {total}, excluded is {len(excludedPipes)}, loop is {len(loop)-1}, included is {total-len(excludedPipes)-len(loop)+1}')
