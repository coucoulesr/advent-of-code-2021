from collections import defaultdict
import heapq

def get_adjacency_map(matrix):
    """
    Returns a dict mapping location tuples to lists of adjacent locations.
    """
    adjacency_map = defaultdict(list)
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            for delta_y in (-1, 1):
                if 0 <= y + delta_y < len(matrix):
                    adjacency_map[(y, x)].append((y + delta_y, x))
            for delta_x in (-1, 1):
                if 0 <= x + delta_x < len(matrix[y]):
                    adjacency_map[(y, x)].append((y, x + delta_x))
    return adjacency_map

def embiggen_matrix(matrix, size_factor=5):
    """
    Returns the given matrix expanded by the given size_factor such that the
    area of the returned matrix is size_factor times the area of the given
    matrix.
    """
    max_increment = (size_factor - 1) * 2
    incremented_matrices = [list(matrix)]
    for i in range(max_increment):
        incremented_matrix = [
            [(val % 9) + 1 for val in row]
            for row in incremented_matrices[i]
        ]
        incremented_matrices.append(incremented_matrix)
    output_matrices = [
        [incremented_matrices[i + j] for i in range(size_factor)]
        for j in range(size_factor)
    ]
    return merge_segmented_matrix(output_matrices)

def merge_segmented_matrix(matrix):
    """
    Returns the result of merging the given 4d matrix (2d matrix of 2d
    matrices) to a 2d matrix. Constituent 2d segment matrices should be of
    the same size.
    """
    output = []
    for row in matrix:
        for row_idx in range(len(row[0])):
            curr_row = []
            for cell in row:
                curr_row.extend(cell[row_idx])
            output.append(curr_row)
    return output

def dijkstra(adjacency_map, origin, cost_matrix):
    """
    Returns a dict mapping location tuples to min cost to traverse there
    from given origin with costs given by given adjacency map.
    """
    cost_map = defaultdict(lambda: float('inf'))
    cost_map[origin] = 0
    pqueue = [(0, dest) for dest in adjacency_map[origin]]
    while pqueue:
        prev_cost, curr = heapq.heappop(pqueue)
        path_cost = prev_cost + cost_matrix[curr[0]][curr[1]]
        if cost_map[curr] > path_cost:
            cost_map[curr] = path_cost
            for dest in adjacency_map[curr]:
                heapq.heappush(pqueue, (path_cost, dest))
    return cost_map

def part1():
    matrix = []
    with open('input15', 'r') as f:
        for line in f:
            line_list = []
            for char in line.strip():
                line_list.append(int(char))
            matrix.append(line_list)
    adjacency_map = get_adjacency_map(matrix)            
    cost_map = dijkstra(adjacency_map, (0, 0), matrix)
    return cost_map[(len(matrix) - 1, len(matrix[0]) - 1)]

def part2():
    matrix = []
    with open('input15', 'r') as f:
        for line in f:
            line_list = []
            for char in line.strip():
                line_list.append(int(char))
            matrix.append(line_list)
    matrix = embiggen_matrix(matrix)
    adjacency_map = get_adjacency_map(matrix)            
    cost_map = dijkstra(adjacency_map, (0, 0), matrix)
    return cost_map[(len(matrix) - 1, len(matrix[0]) - 1)]

print(part1())
print(part2())