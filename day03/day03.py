def parse_bin_array(arr):
    """
    Given an array of binary digits, returns the number's decimal value.
    """
    output = 0
    for idx, val in enumerate(arr[-1::-1]):
        output += (2 ** idx) * int(val)
    return output

def find_by_common(num_set, most_common=True):
    """
    Returns the number from the given set whose number at each index is the
    most common (or least) common number of the numbers in the set.
    """
    index = 0
    next_set = num_set.copy()
    while len(num_set) > 1:
        one_count = 0
        for num in num_set:
            if num[index] == '1':
                one_count += 1
        common = '1' if one_count >= len(num_set) / 2 else '0'
        uncommon = '1' if common == '0' else '0'
        for num in num_set:
            if most_common and num[index] != common:
                next_set.remove(num)
            if not most_common and num[index] != uncommon:
                next_set.remove(num)
        index += 1
        num_set = next_set.copy()
    return num_set.pop()

def part1():
    gamma, epsilon = [], []
    ones_in_pos = None
    with open('input03', 'r') as f:
        line_count = 0
        for line in f:
            if ones_in_pos is None: ones_in_pos = [0] * len(line.strip())
            line_count += 1
            for idx, char in enumerate(line.strip()):
                if char == '1':
                    ones_in_pos[idx] += 1
    for one_count in ones_in_pos:
        gamma.append(0 if one_count < line_count / 2 else 1)
        epsilon.append(0 if one_count >= line_count / 2 else 1)
    return parse_bin_array(gamma) * parse_bin_array(epsilon)

def part2():
    oxygen, co2 = set(), set()
    with open('input03', 'r') as f:
        for line in f:
            oxygen.add(line.strip())
            co2.add(line.strip())
    oxygen = find_by_common(oxygen)
    co2 = find_by_common(co2, most_common=False)
    return parse_bin_array(oxygen) * parse_bin_array(co2)
    
    

print(part1())
print(part2())