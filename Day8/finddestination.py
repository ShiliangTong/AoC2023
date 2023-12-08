import math
import time
class station:
    def __init__(self, name:str, L:str, R:str):
        self.name = name
        self.L = L
        self.R = R

def parseLineToStation(line):
    tmp = line.strip().replace(' ', '').split('=')
    n = tmp[0]
    tmp = tmp[1][1:-1].split(',')
    return station(n, tmp[0], tmp[1])

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day8/input.txt")
pattern = lines[0].strip().replace('\n', '')
stations = {}
for i in range(2, len(lines)):
    st = parseLineToStation(lines[i])
    stations[st.name] = st

#print(f'station {stations["AAA"].name} has L={stations["AAA"].L} and R={stations["AAA"].R}')

steps = 0
currentStation = stations["AAA"]
while currentStation.name != "ZZZ":
    if pattern[steps%len(pattern)] == 'R':
        currentStation = stations[currentStation.R]
    else:
        currentStation = stations[currentStation.L]
    steps += 1
    #print(f'station {currentStation.name} has L={currentStation.L} and R={currentStation.R}')
print(steps)

# Part 2
allStartStations = [st for st in stations.keys() if st.endswith('A')]
allEndstations = [st for st in stations.keys() if st.endswith('Z')]
print(allStartStations)
print(allEndstations)
steps2 = []
currentStations = [stations[name] for name in allStartStations]
for st in currentStations:
    step = 0
    currentStation = st
    while not currentStation.name.endswith('Z'):
        if pattern[step%len(pattern)] == 'R':
            currentStation = stations[currentStation.R]
        else:
            currentStation = stations[currentStation.L]
        step += 1
    print(f'station {st.name} L:{st.L} R:{st.R}, takes {step} to end')
    steps2.append(step)
lcm = math.lcm(*steps2)
print(lcm)

start_time = time.time()
temp = []
stepsCnt = 0
while stepsCnt < 5000:
    temp = []
    for st in currentStations:
        if pattern[stepsCnt%len(pattern)] == 'R':
            temp.append(stations[st.R])
        else:
            temp.append(stations[st.L])
    currentStations = temp
    stepsCnt += 1

end_time = time.time()
execution_time = end_time - start_time

total_execution_time = execution_time * 15746133679061/5000
print(f"Estimated total execution time: {total_execution_time} seconds")
