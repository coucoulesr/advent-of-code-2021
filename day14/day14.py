from collections import Counter

def string_insert(string, sequence, index):
    return string[0:index] + str(sequence) + string[index::]

def transform_polymer(polymer, transformation_map, sequence_length=2):
    insertions_map = dict()
    l, r = 0, sequence_length
    while r <= len(polymer):
        if polymer[l:r] in transformation_map:
            insertions_map[l + sequence_length // 2] = \
                transformation_map[polymer[l:r]]
        l, r = l + 1, r + 1
    offset = 0
    for insertion_idx, insertion in sorted(insertions_map.items(), \
                                           key=lambda x: x[0]):
        polymer = string_insert(polymer, insertion, insertion_idx + offset)
        offset += len(insertion)
    return polymer

def part1():
    with open('input14', 'r') as f:
        polymer = f.readline().strip()
        transformation_map = dict()
        for line in f:
            if line.strip() == '': continue
            sequence, insertion = [val.strip() for val in line.split('->')]
            transformation_map[sequence] = insertion
        for _ in range(10):
            polymer = transform_polymer(polymer, transformation_map)
        letter_count = Counter(polymer)
        return max(letter_count.values()) - min(letter_count.values())

def part2():
    with open('input14', 'r') as f:
        polymer = f.readline().strip()
        transformation_map = dict()

        # Map pairs to list of pairs which replace them
        for line in f:
            if line.strip() == '': continue
            sequence, insertion = [val.strip() for val in line.split('->')]
            transformation_map[sequence] = [
                sequence[0] + insertion,
                insertion + sequence[1]
            ]
        
        # Count pairs in starting polymers
        pairs = Counter()
        for i in range(len(polymer) - 1):
            pairs.update([polymer[i:i+2]])

        for _ in range(40):
            temp = dict(pairs)

            # Change counts based on transformation_map
            for pair, count in temp.items():
                if count > 0 and pair in transformation_map:
                    pairs[pair] -= count
                    for insertion in transformation_map[pair]:
                        pairs[insertion] += count

        # Count number of letters in each pair
        letter_count = Counter(polymer[0] + polymer[-1])
        for pair, count in pairs.items():
            for char in pair:
                letter_count[char] += count

        # Return highest and lowest frequency divided by 2 (pairs)
        return (max(letter_count.values()) - min(letter_count.values())) // 2

print(part1())
print(part2())