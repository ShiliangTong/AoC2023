cardValueMap = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2} 
cardValueMap2 = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2} 

def getType(hand: str):
    distinct = list(set(hand))
    if len(distinct) == 1:
        return 6     # Five of a Kind
    elif len(distinct) == 2:
        if hand.count(distinct[0]) == 4 or hand.count(distinct[0]) == 1:
            return 5   # Four of a Kind
        else:
            return 4   # Full House
    elif len(distinct) == 3:
        if hand.count(distinct[0]) == 3 or hand.count(distinct[1]) == 3 or hand.count(distinct[2]) == 3:
            return 3   # Three of a Kind
        else:
            return 2   # Two Pair
    elif len(distinct) == 4:
        return 1      # Pair
    else:
        return 0    # High Card
    
# part2 to get type with Joker
def getType2(hand: str):
    distinct = list(set(hand))
    if len(distinct) == 1:
        return 6     # Five of a Kind
    elif len(distinct) == 2:
        if 'J' in distinct:
            return 6  # Five of a Kind
        elif hand.count(distinct[0]) == 4 or hand.count(distinct[0]) == 1:
            return 5   # Four of a Kind
        else:
            return 4   # Full House
    elif len(distinct) == 3:
        if 'J' in distinct:
            if hand.count(distinct[0] ) == 3 or hand.count(distinct[1]) == 3 or hand.count(distinct[2]) == 3 or hand.count('J') == 2:
                return 5
            else:
                return 4
        if hand.count(distinct[0]) == 3 or hand.count(distinct[1]) == 3 or hand.count(distinct[2]) == 3:
            return 3   # Three of a Kind
        else:
            return 2   # Two Pair
    elif len(distinct) == 4:
        if 'J' in distinct: # no matter if 2 J or 1 J, it is 3 of a kind.
            return 3
        else:
            return 1      # Pair
    else:
        if 'J' in distinct: 
            return 1
        else:
            return 0

class handsNbet:
    def __init__(self, hand: str, bet: int, type: int):
        self.hand = hand
        self.bet = bet
        self.type = type
        self.score = self.getscore2() #self.getscore()
    
    def FindType(self):
        return getType(self.hand)
    
    def getscore(self):
        return (
            self.type * 10000000000 +
            cardValueMap[self.hand[0]] * 100000000 +
            cardValueMap[self.hand[1]] * 1000000 +
            cardValueMap[self.hand[2]] * 10000 +
            cardValueMap[self.hand[3]] * 100 +
            cardValueMap[self.hand[4]]
        )
    
    def getscore2(self):
        return (
            self.type * 10000000000 +
            cardValueMap2[self.hand[0]] * 100000000 +
            cardValueMap2[self.hand[1]] * 1000000 +
            cardValueMap2[self.hand[2]] * 10000 +
            cardValueMap2[self.hand[3]] * 100 +
            cardValueMap2[self.hand[4]]
        )
#version 2 to compare hands
def Compare2(handsbet):
    return handsbet.score

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()
#part1
lines = readInputFile("C:\code\priv\python\AoC2023\Day7\input.txt")
AllHands = []
for line in lines:
    temp = line.strip().replace('\n', '').split(" ")
    AllHands.append(handsNbet(temp[0], int(temp[1]), getType(temp[0])))

AllHands = sorted(AllHands, key=Compare2)
sum1 = 0
for i in range(1 , len(AllHands)+1):
    print(f"hand rank{i}: {AllHands[i-1].hand} bet: {AllHands[i-1].bet} type: {AllHands[i-1].type} score: {AllHands[i-1].score}")
    sum1 += AllHands[i-1].bet * i
print(f"sum of all bets: {sum1}")

# Part 2
AllHands2 = []
for line in lines:
    temp = line.strip().replace('\n', '').split(" ")
    AllHands2.append(handsNbet(temp[0], int(temp[1]), getType2(temp[0])))
AllHands2 = sorted(AllHands2, key=Compare2)
sum2 = 0  
for i in range(1 , len(AllHands2)+1):
    print(f"hand rank{i}: {AllHands2[i-1].hand} bet: {AllHands2[i-1].bet} type: {AllHands2[i-1].type} score: {AllHands2[i-1].score}")
    sum2 += AllHands2[i-1].bet * i
print(f"sum of all bets: {sum2}")