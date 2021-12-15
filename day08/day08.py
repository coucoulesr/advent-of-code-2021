def is_subsequence(s1, s2):
    """Returns boolean indicating whether all chars in s1 are in s2"""
    return all([ch in s2 for ch in s1])

def sort_signals(signals):
    """
    Returns a sorted copy of the original signals. Signals are sorted by
    ascending length, then each string is sorted alphabetically.
    """
    return ["".join(sorted(signal)) for signal in signals]

def get_signal_mappings(signals):
    """Returns an array mapping integers 0-9 to an alphabetized signal."""
    mappings = [None] * 10
    signals = sort_signals(signals)

    get_signals_of_length = \
        lambda n : [signal for signal in signals if len(signal) == n]

    # Map symbols of unique length
    mappings[1] = get_signals_of_length(2).pop()
    mappings[4] = get_signals_of_length(4).pop()
    mappings[7] = get_signals_of_length(3).pop()
    mappings[8] = get_signals_of_length(7).pop()

    zero_six_nine_candidates = get_signals_of_length(6)
    for candidate in zero_six_nine_candidates:
        if is_subsequence(mappings[7], candidate):
            if is_subsequence(mappings[4], candidate):
                mappings[9] = candidate
            else:
                mappings[0] = candidate
        else:
            mappings[6] = candidate

    two_three_five_candidates = get_signals_of_length(5)
    for candidate in two_three_five_candidates:
        if is_subsequence(candidate, mappings[9]):
            if is_subsequence(mappings[7], candidate):
                mappings[3] = candidate
            else:
                mappings[5] = candidate
        else:
            mappings[2] = candidate

    return mappings


def part1():
    count = 0
    with open('input08', 'r') as f:
        for line in f:
            signals, output_signals = [
                [val.strip() for val in section.split(' ') if val != '']
                for section in line.split('|')
                ]
            mappings = get_signal_mappings(signals)
            for output_signal in sort_signals(output_signals):
                if mappings.index(output_signal) in [1, 4, 7, 8]:
                    count += 1
    return count

def part2():
    total_sum = 0
    with open('input08', 'r') as f:
        for line in f:
            signals, output_signals = [
                [val.strip() for val in section.split(' ') if val != '']
                for section in line.split('|')
                ]
            mappings = get_signal_mappings(signals)
            num = 0
            for output_signal in sort_signals(output_signals):
                num = num * 10 + mappings.index(output_signal)
            total_sum += num
    return total_sum

print(part1())
print(part2())