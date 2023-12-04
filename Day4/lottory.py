import re
class card:
    def __init__(self, num: int, winQuantity: int):
        self.num = num
        self.winQuantity = winQuantity

def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

def parseLines(lines) -> list[card]:
    matrix = []
    for line in lines:
        line = line.replace('\n', '')
        matches = (int(match.group()) for match in re.finditer(r'(\d+)', line))
        card_num = next(matches)
        winNumbers = [next(matches) for _ in range(10)]
        drawNumbers =  [next(matches) for _ in range(25)]
        drawWins = [draw for draw in drawNumbers if draw in winNumbers]
        winQuantity = len(drawWins)
        matrix.append(card(card_num, winQuantity))
    return matrix

def readInputFile(path: str):
    with open(path, 'r') as file:
        return file.readlines()

lines = readInputFile('Day4/input.txt')
allCards = parseLines(lines)

sumScore = 0
for card in allCards:
    score = (2 ** (card.winQuantity -1)) if card.winQuantity > 0 else 0
    sumScore += score
    #print(f"{card.num}, {card.winQuantity}, {score}")
print(f"{sumScore}")

# Part 2
cardQuantities = {card.num: 1 for card in allCards}
for card in allCards:
    print(f"{card.num}, Q:{cardQuantities[card.num]}, W:{card.winQuantity}")
    for i in range(cardQuantities[card.num]):
        for j in range(card.winQuantity):
            cardQuantities[card.num+j+1] += 1

sumValues = sum(cardQuantities.values())
print(sumValues)
