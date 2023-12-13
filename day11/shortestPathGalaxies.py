import re
import copy
def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day11/input.txt")
stars = []
colOrgLen = len(lines[0])
extendedRowCounts = 0
for i in range(len(lines)):
    r = list(lines[i].strip().replace('\n', ''))
    if '#' in r:
        indices = [[i+extendedRowCounts, m.start()] for m in re.finditer('#', lines[i])]
        stars.extend(indices)
    else: # no star row, increase the row count by 1000000-1
        print(f'no star in row {i}')
        extendedRowCounts += 1000000-1
allColsForStars = set([x[1] for x in stars])
print(f'allColsForStars: len {len(allColsForStars)}')
print(f'extendedRowCounts: {extendedRowCounts}')

noStarCols = [i for i in range(colOrgLen) if not i in allColsForStars]
print(f'noStarCols: {noStarCols}')
for star in stars:
    originalStarCol = star[1]
    for nsc in noStarCols:
        if originalStarCol < nsc:
            break
        else:
            #print(f'star {star[0]},{star[1]}, changed to {star[0]},{ star[1] + 1}')
            star[1] += 1000000-1

print(f'stars: {stars}')

def getMinMoveFromAToB(a: list, b: list):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

total_distance = 0
for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        distance = getMinMoveFromAToB(stars[i], stars[j])
        total_distance += distance

print(f"Total distance between all stars: {total_distance}")

