f = open("input.txt", 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

def count_xmas(line):
    result = 0
    result += line.count("XMAS") + line.count("SAMX")
    return result

result = 0
# horizontal
for l in lines:
    result += count_xmas(l)

# vertical
for i in range(len(lines[0])):
    col = [row[i-1] for row in lines]
    col = ''.join(col)
    result += count_xmas(col)
    
# diagonal
diagonal_map = dict()
diagonal_map2 = dict()
for i, line in enumerate(lines):
    diagonal_map[i] = ""
    diagonal_map[-i] = ""
    diagonal_map2[i] = ""
    diagonal_map2[-i] = ""

for li, line in enumerate(lines):
    for ci, c in enumerate(line):
        index = li-ci
        
        diagonal_map[li-ci] += c
    for ci, c in enumerate(line[::-1]):
        index = li-ci
        diagonal_map2[ci-li] += c

for key in diagonal_map.keys():
    result += count_xmas(diagonal_map[key])
    result += count_xmas(diagonal_map2[key])

print("result: ", result)

# Part 2
def check_xmas(x, y):
    diag1 = ""
    diag2 = ""
    for i in range(-1, 2):
        diag1 += lines[y+i][x+i]
        diag2 += lines[y-i][x+i]

    found = (diag1 == 'MAS' or diag1 == "SAM") and (diag2 == 'MAS' or diag2 == 'SAM')

    return found

result = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        # skip bounds
        if y == 0 or y == (len(lines) - 1) or x == 0 or x == (len(line) -1):
            continue
    
        if c != 'A':
            continue
    
        if check_xmas(x, y):
            result += 1

print("r2: ", result)
