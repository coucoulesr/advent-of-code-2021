def increment_neighbors(matrix, y, x):
    """
    Increments all of the neighbors of the position (y, x) in the given 
    matrix.
    """
    for delta_y in (-1, 0, 1):
        for delta_x in (-1, 0, 1):
            if delta_y == 0 and delta_x == 0: continue
            if 0 <= y + delta_y < len(matrix):
                if 0 <= x + delta_x < len(matrix[y + delta_y]):
                    matrix[y + delta_y][x + delta_x] += 1

def cleanup_flash(matrix):
    """Sets all values greater than 9 to 0 in the given matrix."""
    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if val > 9:
                matrix[row_idx][col_idx] = 0

def process_flash(matrix, has_flashed):
    """Returns the number of octopuses that flash this tick."""
    flash_count = 0
    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if val > 9 and not has_flashed[row_idx][col_idx]:
                flash_count += 1
                has_flashed[row_idx][col_idx] = True
                increment_neighbors(matrix, row_idx, col_idx)
    if flash_count == 0: return 0
    flash_count += process_flash(matrix, has_flashed)
    cleanup_flash(matrix)
    return flash_count

def tick(matrix):
    """
    Executes one time step in the given octopus map.
    Returns the number of flashes that occur during the time step.
    """
    for row_idx, row in enumerate(matrix):
        for col_idx in range(len(row)):
            matrix[row_idx][col_idx] += 1
    has_flashed = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
    return process_flash(matrix, has_flashed)

def part1():
    octopus_map = []
    with open('input11', 'r') as f:
        for line in f:
            current_row = [int(val) for val in line.strip()]
            octopus_map.append(current_row)
    flash_count = 0
    for _ in range(100):
        flash_count += tick(octopus_map)
    return flash_count

def part2():
    octopus_map = []
    with open('input11', 'r') as f:
        for line in f:
            current_row = [int(val) for val in line.strip()]
            octopus_map.append(current_row)
    steps = 0
    while any(any(row) for row in octopus_map):
        tick(octopus_map)
        steps += 1
    return steps

print(part1())
print(part2())