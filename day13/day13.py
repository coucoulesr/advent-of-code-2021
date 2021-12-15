BLANK_CHAR = ' '
FILL_CHAR  = "#"

def enlarge_matrix(matrix, y=None, x=None):
    """
    Returns the given 2d matrix, enlarged to height y and width x, with new
    elements set to BLANK_CHAR. Any dimension not supplied remains unchanged.
    y and x, if given, should be larger than the current dimensions of the
    given matrix.
    """
    if y is None:
        y = len(matrix)
    if x is None:
        x = len(matrix[0])
    output = [[BLANK_CHAR for _ in range(x)] for _ in range(y)]
    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            output[row_idx][col_idx] = val
    return output

def flip_matrix(matrix, direction):
    """
    Returns a matrix that is a mirror of the given matrix, flipped either
    vertically or horizontally based on the given direction.
    """
    if direction == 'vertical':
        return [row for row in matrix[-1::-1]]
    if direction == 'horizontal':
        return [row[-1::-1] for row in matrix]

def merge_matrices(matrix1, matrix2):
    """
    Returns the matrix that results from merging the FILL_CHAR characters
    from matrix2 into matrix1. matrix1 and matrix2 should be of the same
    size.
    """
    output = list(matrix1)
    for row_idx, row in enumerate(matrix2):
        for col_idx, val in enumerate(row):
            if val == FILL_CHAR:
                output[row_idx][col_idx] = val
    return output

def fold_matrix(matrix, dimension, location):
    """
    Folds the given matrix along the given dimension (y or x) at the given
    location (coordinate). Returns the result of the folding operation.
    """
    if dimension == 'y':
        m1 = matrix[0:location]
        m2 = matrix[location+1::]
        m2 = flip_matrix(m2, direction='vertical')
    elif dimension == 'x':
        m1 = [row[0:location] for row in matrix]
        m2 = [row[location+1::] for row in matrix]
        m2 = flip_matrix(m2, direction='horizontal')
    else: return
    return merge_matrices(m1, m2)


def part1():
    paper = [[BLANK_CHAR]]
    with open('input13', 'r') as f:
        for line in f:
            if line.strip() == '': continue
            if line.startswith('fold'):
                dimension, location = [val for val in line[11::].split('=')]
                paper = fold_matrix(paper, dimension, int(location.strip()))
                break
            else:
                x, y = [int(val.strip()) for val in line.split(',')]
                if len(paper) <= y:
                    paper = enlarge_matrix(paper, y=y+1)
                if len(paper[0]) <= x:
                    paper = enlarge_matrix(paper, x=x+1)
                paper[y][x] = FILL_CHAR
    return sum([row.count(FILL_CHAR) for row in paper])

def part2():
    paper = [[BLANK_CHAR]]
    with open('input13', 'r') as f:
        for line in f:
            if line.strip() == '': continue
            if line.startswith('fold'):
                dimension, location = [val for val in line[11::].split('=')]
                paper = fold_matrix(paper, dimension, int(location.strip()))
            else:
                x, y = [int(val.strip()) for val in line.split(',')]
                if len(paper) <= y:
                    paper = enlarge_matrix(paper, y=y+1)
                if len(paper[0]) <= x:
                    paper = enlarge_matrix(paper, x=x+1)
                paper[y][x] = FILL_CHAR
    return paper

print(part1())
for line in part2():
    for val in line:
        print(val, end='')
    print()