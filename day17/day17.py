def simulate(v_y, v_x, y_min, y_max, x_min, x_max):
    """
    Returns the result maximum y seen when running a simulation with the
    given starting parameters if the starting parameters lead to a hit.
    If the starting parameters miss, returns None.
    """
    y, x = 0, 0
    highest_y = float('-inf')
    while x < x_max and y > y_min:
        x, y = x + v_x , y + v_y
        if highest_y < y: highest_y = y
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return highest_y
        v_x = v_x - 1 if v_x > 0 else 0
        v_y -= 1
    return None

def brute_force(y_min, y_max, x_min, x_max):
    """
    Runs a simulation for all reasonable starting velocity values.
    Returns a set of velocities which hit target and the highest y reached
    for that velocity pair.
    """
    good_velocities = set()
    for v_x in range(x_max + 1):
        for v_y in range(y_min, 2000):
            highest_y = simulate(v_y, v_x, y_min, y_max, x_min, x_max)
            if highest_y is not None:
                good_velocities.add((v_y, v_x, highest_y))
    return good_velocities

def part1():
    with open('input17') as f:
        line = f.readline().replace('target area: ', '')
        x_params, y_params = [val.strip() for val in line.split(', ')]
        x_min, x_max = [int(val) for val in x_params[2::].split('..')]
        y_min, y_max = [int(val) for val in y_params[2::].split('..')]
        good_velocities = brute_force(y_min, y_max, x_min, x_max)
        return max([velocity[2] for velocity in good_velocities])
    
def part2():
    with open('input17') as f:
        line = f.readline().replace('target area: ', '')
        x_params, y_params = [val.strip() for val in line.split(', ')]
        x_min, x_max = [int(val) for val in x_params[2::].split('..')]
        y_min, y_max = [int(val) for val in y_params[2::].split('..')]
        good_velocities = brute_force(y_min, y_max, x_min, x_max)
        return len(good_velocities)

print(part1())
print(part2())