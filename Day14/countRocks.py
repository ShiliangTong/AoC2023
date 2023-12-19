import time
import csv
from collections import Counter


def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

map = readInputFile("c:/code/priv/python/AoC2023/Day14/input.txt")

def moveLeft(mapIn : []):
    Col = len(mapIn[0])
    Row = len(mapIn)
    mapOut = []
    for i in range(Row):
        # find all '#' in the row and add its index to a list
        indices = [index for index, char in enumerate(mapIn[i]) if char == '#']
        #print(f'indices: {indices}')
        LineAfterNorthMovement = list(mapIn[i])
        openspace = 0
        for j in range(Col):
            if j in indices:
                openspace = 0
                continue
            else:
                if LineAfterNorthMovement[j] == '.':
                    openspace +=1
                    continue
                else:
                        if openspace > 0:
                            LineAfterNorthMovement[j-openspace] = LineAfterNorthMovement[j]
                            LineAfterNorthMovement[j] = '.'
                        else:
                            continue 
        mapOut.append(LineAfterNorthMovement)
    return mapOut

def CheckWeight(mapIn : []):
    sum0 = 0
    Col = len(mapIn[0])
    Row = len(mapIn)
    for i in range(Row):
        # count how many '0's in the row
        count = len([char for char in mapIn[i] if char == 'O'])
        sum0 += count * (Row-i)
    return sum0

def getTransposeMatric(mapIn: []):
    rotated_pattern = list(zip(*mapIn[::1]))
    return rotated_pattern 
    
def getReversedTransposeMatric(mapIn: []):
    rotated_pattern = list(zip(*mapIn[::-1]))
    return rotated_pattern  

def getReversedMatric(mapIn: []):
    return [line[::-1] for line in mapIn]

# print('\n'.join([''.join(line) for line in getReversedMatric(map)]))
# print('------------------------')
# print('\n'.join([''.join(line) for line in getTransposeMatric(map)]))
# print('------------------------')
# print('\n'.join([''.join(line) for line in getReversedTransposeMatric(map)]))
def find_repeating_sublist(lst):
    length = len(lst)
    for sublist_length in range(1, length // 2 + 1):
        sublist = lst[:sublist_length]
        if lst == sublist * (length // sublist_length) + sublist[:length % sublist_length]:
            return 0, sublist
    for i in range(1, length):
        for sublist_length in range(1, (length - i) // 2 + 1):
            sublist = lst[i:i+sublist_length]
            remaining_list = lst[i:]
            if remaining_list == sublist * ((length - i) // sublist_length) + sublist[:(length - i) % sublist_length]:
                return i, sublist
    return -1, []

CycleScore = []
for i in range(500):
    #move north
    tempMap = getTransposeMatric(map)
    tempMap = moveLeft(tempMap)   
    #move west
    temp2 = getTransposeMatric(tempMap)
    temp2 = moveLeft(temp2)
    #move south
    temp3 = getReversedTransposeMatric(temp2)
    temp3 = moveLeft(temp3)
    #move east
    temp4 = getReversedTransposeMatric(getReversedMatric(temp3))
    map = moveLeft(temp4)
    #rotate back
    map = getReversedMatric(map)
    #print('\n'.join([''.join(line) for line in map]))

    temp = CheckWeight(map)
    print(f"score of round {i+1}: {temp}")
    CycleScore.append(temp)

idx, subList = find_repeating_sublist(CycleScore)
print(f"Start point of repetition: {idx}")
print(f"repetition sublist: {subList}")

#calculate the score at index 1000000000 -1 
print(f"score: {CycleScore[(1000000000 - idx) % len(subList) + idx - 1]}")
# end_time = time.time()
# execution_time = end_time - start_time
# total_execution_time = execution_time * 1000000000/3600000
# print(f"Estimated total execution time: {total_execution_time} hours")



