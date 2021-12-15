def part1():
    y, x = 0, 0
    with open('input02', 'r') as f:
        for line in f:
            direction, magnitude = line.split(' ')
            if direction == 'forward':
                x += int(magnitude)
            else: # direction == up or direction == down 
                negation_factor = -1 if direction == 'up' else 1
                y += negation_factor * int(magnitude)
    return y * x

def part2():
    y, x, aim = 0, 0, 0
    with open('input02', 'r') as f:
        for line in f:
            direction, magnitude = line.split(' ')
            if direction == 'forward':
                x += int(magnitude)
                y += int(magnitude) * aim
            else: # direction == up or direction == down 
                negation_factor = -1 if direction == 'up' else 1
                aim += negation_factor * int(magnitude)
    return y * x

print(part1())
print(part2())