data = [list(l) for l in open('input.txt').read().splitlines()]

inverted = list(zip(*data))
diag = [[] for _ in range(len(data) + len(data[0]) - 1)]
antidiag = [[] for _ in range(len(diag))]

min_bdiag = -len(data) + 1
for y, row in enumerate(data):
    for x, val in enumerate(row):
        diag[x + y].append(val)
        antidiag[x - y - min_bdiag].append(val)

# print(antidiag)
count = 0
for matrice in [diag]:
    for line in matrice:
        line = ''.join(line)
        count += line.count('XMAS') + line.count('SAMX')

print(count)