f = open("input.txt", 'r')
lines = [l.strip() for l in f.readlines()]

antenna_symbols = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
antenna_map = dict()
for s in antenna_symbols:
    antenna_map[s] = []

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            antenna_map[c].append((x, y))

antinode_positions = []
antinode_positions2 = []


def in_bounds(pos):
    min_x = 0
    min_y = 0
    max_x = len(lines[0])
    max_y = len(lines)
    return pos[0] >= min_x and pos[1] >= min_y and pos[0] < max_x and pos[1] < max_y


def filter_valid_positions(ps):
    result = []
    for p in ps:
        if in_bounds(p):
            result.append(p)
    return result


def calc_antinodes(pos, other):
    antinodes = []
    (x1, y1) = pos
    for (x2, y2) in other:
        (dx, dy) = (x1-x2, y1-y2)
        antinodes.append((x2+2*dx, y2+2*dy))
        antinodes.append((x2-dx, y2-dy))
    return antinodes


def calc_antinodes2(pos, other):
    antinodes = [pos]
    (x1, y1) = pos

    for (x2, y2) in other:
        antinodes.append((x2, y2))
        (dx, dy) = (x1-x2, y1-y2)

        new_pos_l = (x2+2*dx, y2+2*dy)
        while (in_bounds(new_pos_l)):
            antinodes.append(new_pos_l)
            new_pos_l = (new_pos_l[0] + dx, new_pos_l[1] + dy)

        new_pos_r = (x2-dx, y2-dy)
        while (in_bounds(new_pos_r)):
            antinodes.append(new_pos_r)
            new_pos_r = (new_pos_r[0] - dx, new_pos_r[1] - dy)
    return antinodes


for key in antenna_map:
    positions = antenna_map[key]
    for i, pos in enumerate(positions[:-1]):
        other = positions[i+1:]
        antinode_positions += calc_antinodes(pos, other)
        antinode_positions2 += calc_antinodes2(pos, other)

antinode_positions = filter_valid_positions(antinode_positions)
print(len(set(antinode_positions)))
print(len(set(antinode_positions2)))
