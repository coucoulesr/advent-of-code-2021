def first_corrupted_char(line):
    """
    Returns the index of the first corrupted character in the line, if it
    exists.
    """
    opening_chars = ('(', '[', '{', '<')
    closing_chars = (')', ']', '}', '>')
    stack = []
    for idx, char in enumerate(line):
        if char in opening_chars:
            stack.append(char)
            continue
        if char in closing_chars:
            opening_char = opening_chars[closing_chars.index(char)]
            if stack[-1] != opening_char:
                return idx
            stack.pop()

def get_completion_chars(line):
    """Returns the string of characters which completes the given line."""
    opening_chars = ('(', '[', '{', '<')
    closing_chars = (')', ']', '}', '>')
    stack = []
    for char in line:
        if char in opening_chars:
            stack.append(char)
            continue
        if char in closing_chars:
            stack.pop()

    # Reverse stack and replace with corresponding closing chars
    stack = stack[-1::-1]
    stack = [closing_chars[opening_chars.index(char)] for char in stack]
    return "".join(stack)

def part1():
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total_score = 0
    with open('input10', 'r') as f:
        for line in f:
            if first_corrupted_char(line):
                total_score += scores[line[first_corrupted_char(line)]]
    return total_score

def part2():
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    total_scores = []
    with open('input10', 'r') as f:
        for line in f:
            current_score = 0
            if not first_corrupted_char(line):
                for char in get_completion_chars(line):
                    current_score *= 5
                    current_score += scores[char]
                total_scores.append(current_score)
    return sorted(total_scores)[len(total_scores) // 2]

print(part1())
print(part2())