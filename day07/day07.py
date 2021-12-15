def part1():
    cheapest_total = float('inf')
    with open('input07', 'r') as f:
        positions = [int(val.strip()) for val in f.read().split(',')]
    for p1 in range(max(positions) + 1):
        total_cost = sum([abs(p2 - p1) for p2 in positions])
        if total_cost < cheapest_total:
            cheapest_total = total_cost
    return cheapest_total

def part2():
    fuel_fn = lambda n : sum(range(n+1))
    cheapest_total = float('inf')
    with open('input07', 'r') as f:
        positions = [int(val.strip()) for val in f.read().split(',')]
    for p1 in range(max(positions) + 1):
        total_cost = sum([fuel_fn(abs(p2 - p1)) for p2 in positions])
        if total_cost < cheapest_total:
            cheapest_total = total_cost
    return cheapest_total

print(part1())
print(part2())