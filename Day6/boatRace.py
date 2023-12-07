import re
class record:
    def __init__(self, time: int, maxDist: int):
        self.time = time
        self.maxDist = maxDist

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("C:\code\priv\python\AoC2023\Day6\input.txt")
times = list(map(int, re.findall(r'\d+', lines[0])))
maxDists = list(map(int, re.findall(r'\d+', lines[1])))

records = []
for time, maxDist in zip(times, maxDists):
    records.append(record(time, maxDist))

def getDistance(pressedtime: int, totalTime: int) -> int:
    return pressedtime * (totalTime - pressedtime)

def getWaysToBeatRecord(record: record) -> []: # return ways and max distance
    ways = maxDistance = 0
    for i in range(record.time-1, 0, -1):
        dis = getDistance(i, record.time)
        if dis > record.maxDist:
            maxDistance = dis if dis > maxDistance else maxDistance
            ways += 1
        elif ways > 1:
            return ways, maxDistance
    return ways

result = 1
for rec in records:
    ways, maxDistance = getWaysToBeatRecord(rec)
    result *= ways
    print(f"record: {rec.time} {rec.maxDist} ways: {ways} maxDistance: {maxDistance}")
print(f"result: {result}")

# Part 2
time = int(lines[0].replace(' ', '').replace('Time:', ''))
dist = int(lines[1].replace(' ', '').replace('Distance:', ''))
record_obj = record(time, dist)

ways, maxDistance = getWaysToBeatRecord(record_obj)
print(f"record: {time} {maxDistance} ways: {ways} maxDistance: {maxDistance}")
