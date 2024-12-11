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

for v in val_set:
    has_seen_map[v] = False

for k in key_set:
    rule_map[k] = []

for [k,v] in rules:
    rule_map[k].append(v)

def calculate_update(update):
    for number in update:
        order_values = rule_map.get(number, [])
        if order_values == None: 
            order_values = []
        
        for ov in order_values:
            if has_seen_map.get(ov, False) == True:
                return 0
        
        has_seen_map[number] = True
    
    return update[int(len(update)/2)]


result = 0
for update in updates:
    result += calculate_update([int(x) for x in update.split(',')])
    # Reset has_seen_map
    for k in has_seen_map:
        has_seen_map[k] = False

print("res1 " , result)