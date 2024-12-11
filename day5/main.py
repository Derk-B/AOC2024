f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]
rules = []
for line in lines:
    if line == '':
        break
    rules.append(line)
updates = lines[len(rules) + 1:]

rule_map = dict()
has_seen_map = dict()
rules = [[int(a), int(b)] for [a, b] in [rule.split('|') for rule in rules]]

key_set = set([k for [k, v] in rules])
val_set = set([v for [k, v] in rules])

for k in key_set:
    rule_map[k] = []

for [k,v] in rules:
    rule_map[k].append(v)

def calculate_update(update):
    # Reset has_seen_map
    for k in has_seen_map:
        has_seen_map[k] = None

    for i, number in enumerate(update):
        order_values = rule_map.get(number, [])
        
        for ov in order_values:
            if has_seen_map.get(ov, None) != None:
                return 0
        
        has_seen_map[number] = i
    
    return update[int(len(update)/2)]

def check_position(order_values, numbers, number, i):
    for ov in order_values:
        conflict_index = has_seen_map.get(ov, None)
        if conflict_index != None:
            numbers[i] = ov
            numbers[conflict_index] = number
            return numbers

def part2(update):
    update_numbers = update
    # Reset has_seen_map
    for k in has_seen_map:
        has_seen_map[k] = None
    
    for i, number in enumerate(update_numbers):
        order_values = rule_map.get(number, [])
        new_array = check_position(order_values, update_numbers, number, i)
        if new_array != None:
            return part2(new_array)
            
        has_seen_map[number] = i

    return update_numbers[int(len(update)/2)]

result = 0
result2 = 0
for update in updates:
    numbers = [int(x) for x in update.split(',')]
    ordered_result = calculate_update(numbers)
    if ordered_result == 0:
        result2 += part2(numbers)
    else:
        result += ordered_result


print("res1 " , result)
print('res2 ', result2)