def part1():
    with open("input01", "r") as f:
        last_seen = float('inf')
        times_increased = 0
        for line in f:
            if int(line) > last_seen:
                times_increased += 1
            last_seen = int(line)
    return times_increased

def part2():
    with open("input01", "r") as f:
        times_increased = 0
        window_size = 3
        window = [None] * window_size

        # Get window initial values
        for i in range(window_size):
            window[i] = int(f.readline().strip())
        window_sum = sum(window)
        prev_window_sum = window_sum

        for line in f:
            # Move window
            window_sum -= window[0]
            for i in range(window_size - 1):
                window[i] = window[i + 1]
            window[window_size - 1] = int(line)
            window_sum += window[window_size - 1]

            # Check if sum increased
            if window_sum > prev_window_sum:
                times_increased += 1
            prev_window_sum = window_sum
    return times_increased

print(part1())
print(part2())