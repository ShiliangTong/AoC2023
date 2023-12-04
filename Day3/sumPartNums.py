import re
class number:
    def __init__(self, value: int, row: int, start_index: int, length: int, isPartNumber: bool):
        self.value = value
        self.row = row
        self.start_index = start_index
        self.length = length
        self.isPartNumber = isPartNumber


def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

def parseLines(lines) -> list[number]:
    matrix = []
    for i in range(len(lines)):
        line = lines[i].replace('\n', '') 
        matches = re.finditer(r'(\d+)', line)
        for match in matches:
            val = int(match.group())
            start_index=match.start()
            length = len(match.group())
            lenLine = len(line)
            #print(lenLine)
            isLinkedToSymbol = (start_index!=0 and line[start_index-1] != '.') or (start_index+length != lenLine and line[start_index+length] != '.')
            
            #print(f"{val}, {i}, {start_index}, {length}, {isLinkedToSymbol}")
            
            matrix.append(number(val, i, start_index, length, isLinkedToSymbol))
    return matrix

def isStringContainsSymbols(string: str, start_idx: int, end_idx: int):
    strLine = string.replace('\n', '')
    safeStartIdx = start_idx-1 if start_idx-1 > 0 else 0
    safeEndIdx = end_idx+1 if end_idx+1 < len(strLine) else len(strLine)
    for char in strLine[safeStartIdx:safeEndIdx]:
        if not char.isdigit() and char != '.':
            return True
    return False


# Part 1
#lines = readInputFile("./input.txt")
strTest1 = "...................#386...=........313........-...&............*......*................@.............../.........621+......................."
strTest2 = "*...*.......................885.....*...123.=...641...&188..577.......339..688.........287.684..219.........................+............250"
strTest3 = "..........535...541=........*.......696..@..323..................93=.......*.......30......*....*......-........+.222$.......458.817........"
lines = readInputFile("C:\code\priv\python\AoC2023\Day3\input.txt") 
#lines= [strTest1, strTest2, strTest3]
matrix = parseLines(lines)
sum1=0
for num in matrix:
    if not num.isPartNumber:
        if num.row != 0 and isStringContainsSymbols(lines[num.row-1],num.start_index, num.start_index+num.length):
            num.isPartNumber = True
        elif num.row != len(lines)-1 and isStringContainsSymbols(lines[num.row+1],num.start_index, num.start_index+num.length):
            num.isPartNumber = True
        # else:          
        #     print(f"{num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")

    sum1 += num.value if num.isPartNumber else 0

print(sum1)

# Part 2
sum2 = 0
maxtrix2 = []
from collections import defaultdict
starCollection = defaultdict(list)
for i in range(len(lines)):
    line = lines[i].replace('\n', '') 
    matches = re.finditer(r'(\d+)', line)
    for match in matches:
        val = int(match.group())
        start_index=match.start()
        length = len(match.group())
        lenLine = len(line)
        #print(lenLine)
        isLinkedToSymbol = (start_index!=0 and line[start_index-1] != '.') or (start_index+length != lenLine and line[start_index+length] != '.')
        num = number(val, i, start_index, length, isLinkedToSymbol)
        if isLinkedToSymbol: 
            if (start_index!=0 and line[start_index-1] == '*'):
                starCollection[f"{i}:{start_index-1}"].append(num)
                print(f"*({i},{start_index-1}) added {num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")
            if (start_index+length != lenLine and line[start_index+length] == '*'):
                starCollection[f"{i}:{start_index+length}"].append(num)
                print(f"*({i},{start_index+length}) added {num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")

        #print(f"{val}, {i}, {start_index}, {length}, {isLinkedToSymbol}")
        
        maxtrix2.append(num)

for num in maxtrix2:

    if num.row != 0:
        strLine = lines[num.row-1].replace('\n', '')
        endIdx = num.start_index+num.length + 1
        safeStartIdx = num.start_index-1 if num.start_index-1 > 0 else 0
        safeEndIdx = endIdx if endIdx < len(strLine) else len(strLine)
        subStr = strLine[safeStartIdx:safeEndIdx]
        for i in range(len(subStr)):
            if subStr[i] == '*' :
                starCollection[f"{num.row-1}:{safeStartIdx + i}"].append(num)
                print(f"*({num.row-1},{safeStartIdx + i}) added {num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")
        
    if num.row != len(lines)-1:
        strLine = lines[num.row+1].replace('\n', '')
        endIdx = num.start_index+num.length + 1
        safeStartIdx = num.start_index-1 if num.start_index-1 > 0 else 0
        safeEndIdx = endIdx if endIdx < len(strLine) else len(strLine)
        subStr = strLine[safeStartIdx:safeEndIdx]
        for i in range(len(subStr)):
            if subStr[i] == '*' :
                starCollection[f"{num.row+1}:{safeStartIdx + i}"].append(num)
                print(f"*({num.row+1},{safeStartIdx + i}) added {num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")
          
    #print(f"{num.value}, {num.row}, {num.start_index}, {num.length}, {num.isPartNumber}")

    #sum1 += num.value if num.isPartNumber else 0
pairs_with_two_elements = [(key, value) for key, value in starCollection.items() if len(value) == 2]

sum_of_multiples = 0

for key, value in pairs_with_two_elements:
    num1, num2 = value
    multiple = num1.value * num2.value
    sum_of_multiples += multiple

print(sum_of_multiples)


print(len(pairs_with_two_elements))