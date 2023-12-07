import re
class range_start_end:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class mapResult:
    def __init__(self, mapped: list, unmapped: list):
        self.mapped = mapped
        self.unmapped = unmapped

class SourceDesRangePair:
    def __init__(self, destination: int, source_start: int,  range: int):
        self.source_start = source_start
        self.destination = destination
        self.end = source_start + range
    
    def translate(self, val: int) -> int:
        return self.destination + (val - self.source_start)

    def GetDestination(self, val: int) -> int:
        if self.source_start <= val <= self.end:
            return self.translate(val)
        else:
            return -1
    def GetDestinationPart2(self, ran: range_start_end) -> mapResult:
        if self.source_start <= ran.start <= self.end:
            if self.source_start <= ran.end and ran.end <= self.end:
                return mapResult([range_start_end(self.translate(ran.start), self.translate(ran.end))], [])
            else:
                return mapResult([range_start_end(self.translate(ran.start), self.translate(self.end))], [range_start_end(self.end + 1, ran.end)])
        elif self.source_start <= ran.end and ran.end <= self.end:
            return mapResult([range_start_end(self.translate(self.source_start), self.translate(ran.end))], [range_start_end(ran.start, self.source_start - 1)])
        else:
            return mapResult([], [range_start_end(ran.start, ran.end)])

class Map:
    def __init__(self, PairList: list[SourceDesRangePair]):
        self.PairList = PairList

def SearchDestinationPart3(pairs: list[SourceDesRangePair], range: range_start_end) -> list[range_start_end]:
    mapSt = mapResult([], [range])
    for pair in pairs:
        new_unmapped = []
        for i, unmapped_range in enumerate(mapSt.unmapped):
            # Ensure unmapped_range is a range_start_end object
            if isinstance(unmapped_range, range_start_end):
                mapResultTemp = pair.GetDestinationPart2(unmapped_range)
                if mapResultTemp.mapped:
                    mapSt.mapped.extend(mapResultTemp.mapped)
                if mapResultTemp.unmapped:
                    new_unmapped.extend(mapResultTemp.unmapped)
            else:
                print(f"Error: Expected a range_start_end object, but got {type(unmapped_range)}")
        mapSt.unmapped = new_unmapped
    if mapSt.unmapped:
        mapSt.mapped.extend(mapSt.unmapped)
        mapSt.unmapped = []
    return mapSt.mapped

def SearchDestinationPart4(pairs: list[SourceDesRangePair], unmapped: list[range_start_end]) -> list[range_start_end]:
    result = []
    for st_end in unmapped:
        result.extend(SearchDestinationPart3(pairs, st_end))
    return result

def SearchDestination(pairs: list[SourceDesRangePair], val: int) -> int:
    # below could be optimized by sorting the list by source, and then using binary search to find the pair
    for pair in pairs:
        if pair.GetDestination(val) != -1:
            return pair.GetDestination(val)
    return val

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

def parselineToPair(line: str):
    temp = line.strip().replace('\n', '').split(" ")
    pair = SourceDesRangePair(int(temp[0]), int(temp[1]), int(temp[2]))
    return pair

lines = readInputFile("C:\code\priv\python\AoC2023\Day5\input.txt")
seeds = []
matches = re.findall(r'\d+', lines[0])
seeds.extend(matches)
print(seeds)

sections = []
current_section = []
for line in lines[2:]:
    if line.strip() == "":
        if current_section:
            sections.append(Map(current_section))
            current_section = []
    else:
        if ':' in line:
            print(f"section {line.strip()} started ")
        else:
            current_section.append(parselineToPair(line))
if current_section:
    sections.append(Map(current_section))

MinLocation = 1382789085
for seed in seeds:
    start  = seed
    for sec in sections:
        mapVal = SearchDestination(sec.PairList, int(start))
        start = mapVal
    location = start
    if location < MinLocation:
        MinLocation = location
        #print(f"MinLocation: {MinLocation}")

print(f"MinLocation: {MinLocation}")

# Part 2
def convertSeedsToRanges(seeds: list[int]) -> list[range_start_end]:
    ranges = []
    for i in range(int(len(seeds)/2)):
        ranges.append(range_start_end(int(seeds[i*2]), int(seeds[i*2]) + int(seeds[i*2+1])))
    return ranges

ranges = convertSeedsToRanges(seeds)
print(f"start of ranges: {len(ranges)}")

result = ranges
for sec in sections:
    result = SearchDestinationPart4(sec.PairList, result)
    print(f"end of mapping for a section: mapped ranges {len(result)}")

min_start = min([r.start for r in result])   
print(f"Minimum start value: {min_start}")

