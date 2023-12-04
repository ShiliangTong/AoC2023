import re

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

# Part 1
def sumline(line: str) -> int:
    digits = re.findall(r'\d', line)
    return int(digits[0])*10 + int(digits[-1])

lines = readInputFile("./input.txt")

sum = 0
for line in lines:
    sum += sumline(line)
print(sum)

# Part 2
num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

def find_substring_start_index(string: str, substring: str) -> int:
    match = re.search(substring, string)
    if match:
        return match.start()
    else:
        return 99
def convertKeySpellsToNums(line: str) -> str:
    line = line.lower()

    SpeltNum_1st = 99
    SpeltNum_1st_key = ''
    SpeltNum_last = 99
    SpeltNum_last_key = ''
    
    for key in num_dict.keys():
        # for the case like threeight, sevenine, shared characters
        match1st_idx = find_substring_start_index(line, key)
        if match1st_idx < SpeltNum_1st:
            SpeltNum_1st = match1st_idx
            SpeltNum_1st_key = key
        matchLast_idx = find_substring_start_index(line[::-1], key[::-1])
        if matchLast_idx < SpeltNum_last:
            SpeltNum_last = matchLast_idx
            SpeltNum_last_key = key
    if SpeltNum_1st != 99:
        line = line[:SpeltNum_1st] + num_dict[SpeltNum_1st_key]  + line[SpeltNum_1st + len(SpeltNum_1st_key):]
    if SpeltNum_last != 99:
        line = line[:-(SpeltNum_last+len(SpeltNum_last_key))] + num_dict[SpeltNum_last_key] + line[len(line)-SpeltNum_last:]
    return line


sum2 = 0
for line in lines:
    sum2 += sumline(convertKeySpellsToNums(line))

print(sum2)
