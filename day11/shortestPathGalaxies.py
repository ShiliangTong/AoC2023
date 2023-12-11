import re
import copy
def readInputFile(path: str):
    file = open(path, 'r')
    return file.readlines()

lines = readInputFile("c:/code/priv/python/AoC2023/Day11/input.txt")
stars = []
matrix = []
for i in range(len(lines)):
    r = list(lines[i].strip().replace('\n', ''))
    matrix.append(r)
    if '#' in r:
        indices = [(i, m.start()) for m in re.finditer('#', lines[i])]
        print(indices)
        stars.extend(indices)
    else: # no star row, add empty row with '.'s
        print(f'no star in row {i}, add empty row')
        matrix.append(r)

expandedMatrix_col = copy.deepcopy(matrix)
star_cols = set()  # Set to store unique column numbers of stars
cnt_expanded_col = 0
for col in range(len(matrix[0])):
    col_str = ''.join([row[col] for row in matrix])
    print(f'col {col}: {col_str}')
    if not '#' in col_str:
        print(f'no star in col {col}, add empty col')
        for row in range(len(matrix)):
            expandedMatrix_col[row].insert(col+cnt_expanded_col, '.')
        cnt_expanded_col += 1
    else:
        star_cols.add(col)  # Add the column number to the set
        print(f'star in col {col}')

distinct_cols = len(star_cols)  # Get the count of unique column numbers
print(f"Distinct column numbers of stars: {distinct_cols}")

