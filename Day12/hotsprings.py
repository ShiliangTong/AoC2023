import re
import itertools
def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

def getPotentialAmountofMaps(map: str, result: list):
    possibilities = itertools.product('#.', repeat=map.count('?'))
    potentialMaps = 0
    for possibility in possibilities:
        new_map = map.replace('?', '{}').format(*possibility)
        #print(new_map)
        if isMapValid(new_map, result):
            #print(f'new_map{new_map} is valid for result {result}')
            potentialMaps += 1
    return potentialMaps

def isMapValid(map: str, result: list):
    splited = list(filter(None, map.split('.')))
    if len(splited) == len(result) and all([len(splited[x]) == result[x] for x in range(len(splited))]):
        return True
    return False


# def FirstLogicOperation(map: str, result: list):


lines = readInputFile("c:/code/priv/python/AoC2023/Day12/input.txt")
sum0 = 0
#     ?#???#?..???# 2,1,1,1
for i in range(len(lines)):
    tmp = lines[i].strip().replace('\n', '').split(' ')
    mapResult = [int(x) for x in tmp[1].split(',')] 
    map = tmp[0]
    potCount = getPotentialAmountofMaps(map, mapResult)
    sum0 += potCount
    #print(f'map: {map}, result: {mapResult}, potential amount of maps: {potCount}')

print(f'sum0: {sum0}')