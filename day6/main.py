f = open("input.txt", 'r')
lines = [list(line.strip()) for line in f.readlines()]

guard_pos = (0, 0)
# Starting direction (up)
guard_direction = (0, -1)

# part 2
direction_map = dict()
obstacle_list = []

# Find guard starting pos
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '^':
            guard_pos = (x, y)
            break

def turn_right(dir):
    match dir:
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)
        
def out_of_bounds(pos):
    if pos[1] >= len(lines):
        return True
    if pos[1] < 0:
        return True
    if pos[0] >= len(lines[0]):
        return True
    if pos[0] < 0:
        return True
    return False

def will_enter_loop(dir):
    temp_pos = guard_pos
    while temp_pos != '#' and not out_of_bounds(temp_pos):
        # print("temp: ", temp_pos, guard_pos, out_of_bounds(temp_pos))
        if direction_map.get(temp_pos, None) == dir:
            return True
        temp_pos = (temp_pos[0] + dir[0], temp_pos[1] + dir[1])
        
    return False

while not out_of_bounds(guard_pos):
    lines[guard_pos[1]][guard_pos[0]] = 'X'
    look_ahead = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

    # part 2
    look_right_dir = turn_right(guard_direction)
    if (not out_of_bounds(look_ahead) and lines[look_ahead[1]][look_ahead[0]] != '#' and will_enter_loop(look_right_dir)):
        obstacle_list.append(look_ahead)
    # end part 2

    if (not out_of_bounds(look_ahead) and lines[look_ahead[1]][look_ahead[0]] == '#'):
        guard_direction = turn_right(guard_direction)

    # part 2
    direction_map[guard_pos] = guard_direction
    # end part 2

    guard_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

for (x, y) in obstacle_list:
    lines[y][x] = 'O'
out = open("out.txt", 'w')
out.writelines([''.join(line) + "\n" for line in lines])

result1 = 0
result2 = 0
for line in lines:
    for c in line:
        if c == 'X' or c == 'O':
            result1 += 1
        if c == 'O':
            result2 += 1
print("part 1: ", result1)
print('part 2: ', result2)
