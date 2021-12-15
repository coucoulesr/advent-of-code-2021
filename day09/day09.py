from functools import reduce

def is_local_min(matrix, row, col):
    """
    Returns a boolean indicating whether the object at the given row and 
    column is smaller than all adjacent objects in the matrix. Checks left,
    right, up, and down adjacencies.
    """
    for delta_y in (-1, 1):
        if 0 <= row + delta_y < len(matrix):
            if matrix[row][col] >= matrix[row + delta_y][col]:
                return False
    for delta_x in (-1, 1):
        if 0 <= col + delta_x < len(matrix[row]):
            if matrix[row][col] >= matrix[row][col + delta_x]:
                return False
    return True

def replace_basin(height_map, row, col, symbol):
    """
    Replaces all of the elements in the basin in height_map at position (row,
    col) with the given symbol.
    """
    break_conditions = [
        not 0 <= row < len(height_map),      # OOB Y
        not 0 <= col < len(height_map[row]), # OOB X
        not 0 <= height_map[row][col] < 9    # < 0 already seen; 9 boundary
    ]
    if any(break_conditions): return
    height_map[row][col] = symbol
    for delta_y in (-1, 1):
        replace_basin(height_map, row + delta_y, col, symbol)
    for delta_x in (-1, 1):
        replace_basin(height_map, row, col + delta_x, symbol)

def count_2d(matrix, search_val):
    """Returns the number of occurrences of search_val in given 2d matrix."""
    count = 0
    for line in matrix:
        for val in line:
            if val == search_val:
                count += 1
    return count

def part1():
    local_min_sum = 0
    height_map = []
    with open('input09', 'r') as f:
        for line in f:
            line_map = []
            for height in line.strip():
                line_map.append(int(height))
            height_map.append(line_map)
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if is_local_min(height_map, i, j):
                local_min_sum += 1 + height_map[i][j]
    return local_min_sum

def part2():
    height_map = []
    with open('input09', 'r') as f:
        for line in f:
            line_map = []
            for height in line.strip():
                line_map.append(int(height))
            height_map.append(line_map)

    # replace basins with negative numbers
    symbol = -1
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if 0 <= height_map[i][j] < 9:
                replace_basin(height_map, i, j, symbol)
                symbol -= 1
    
    # get top 3 from highest counts of each negative number
    top3 = [0] * 3
    for symbol_to_count in range(-1, symbol - 1, -1):
        symbol_count = count_2d(height_map, symbol_to_count)
        if symbol_count > min(top3):
            top3[top3.index(min(top3))] = symbol_count
    return reduce(lambda x, y: x * y, top3)

print(part1())
print(part2())