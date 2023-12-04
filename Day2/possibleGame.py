import re

CfgedNumColor = {'blue': 14, 'green': 13, 'red': 12}

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

def extractGameNum(string: str):
    game_num = re.match(r'Game (\d+):', string)
    return int(game_num.group(1))

def maxNumForEachColor(string: str):
    matches = re.findall(r'(\d+)\s+(\w+)', string) 
    maxNumColor = {'blue': 0, 'green': 0, 'red': 0}
    for cnt, color in matches:
        if int(cnt) > maxNumColor[color]:
            maxNumColor[color] = int(cnt)
    return maxNumColor

def impossibleGameID (line: str):
    matches = re.findall(r'(\d+)\s+(\w+)', line) 
    for cnt, color in matches:
        if int(cnt) > CfgedNumColor[color]:
            return 0
    return  extractGameNum(line)

lines = readInputFile("./input.txt")

# Part 1
sum1 = 0
for line in lines:
    sum1 += impossibleGameID(line)
print(sum1)

# Part 2
sum2 = 0
for line in lines:
    minCofig = maxNumForEachColor(line)
    sum2 += minCofig['blue'] * minCofig['green'] * minCofig['red']
print(sum2)