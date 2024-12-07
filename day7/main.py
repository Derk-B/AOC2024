f = open("input.txt", "r")
lines = f.readlines()
calibrations = []

for line in lines:
    [result, instructions] = line.strip().split(": ")
    instructions = [int(x) for x in instructions.split(' ')]
    calibrations.append([int(result), instructions])


def possibilities(value, terms):
    if terms == []:
        return [value]
    res = possibilities(value * terms[0], terms[1:]) + \
        possibilities(value + terms[0], terms[1:]) + \
        possibilities(
            # comment this to get part 1
            int(str(value) + str(terms[0])), terms[1:])
    return res


result = 0
for calibration in calibrations:
    ps = possibilities(calibration[1][0], calibration[1][1:])
    if (calibration[0] in ps):
        result += calibration[0]
print(result)
