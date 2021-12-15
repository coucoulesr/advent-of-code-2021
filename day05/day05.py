from collections import defaultdict

def part1():
    vent_map = defaultdict(int)
    with open('input05', 'r') as f:
        for line in f:
            origin, endpoint = [
                val.strip().split(',')[-1::-1] for val in line.split('->')
                ]
            origin = [int(i) for i in origin]
            endpoint = [int(i) for i in endpoint]
            if origin[0] == endpoint[0]:
                # horizontal
                y = origin[0]

                for x in range(min(origin[1], endpoint[1]),
                               max(origin[1], endpoint[1]) + 1
                              ):
                    vent_map[(y, x)] += 1
            if origin[1] == endpoint[1]:
                # vertical
                x = origin[1]
                for y in range(min(origin[0], endpoint[0]),
                               max(origin[0], endpoint[0]) + 1
                              ):
                    vent_map[(y, x)] += 1
    count = 0
    for val in vent_map.values():
        if val >= 2:
            count += 1
    return count

def part2():
    vent_map = defaultdict(int)
    with open('input05', 'r') as f:
        for line in f:
            origin, endpoint = [
                val.strip().split(',')[-1::-1] for val in line.split('->')
                ]
            origin = [int(i) for i in origin]
            endpoint = [int(i) for i in endpoint]
            delta = [0, 0]
            for coord in (0, 1):
                coord_dir = (endpoint[coord] - origin[coord])
                coord_mag = abs(endpoint[coord] - origin[coord])
                delta[coord] = coord_dir / coord_mag if coord_mag != 0 else 0
            traversal = list(origin)
            vent_map[tuple(traversal)] += 1
            while traversal != endpoint:
                for coord in (0, 1):
                    traversal[coord] += delta[coord]
                vent_map[tuple(traversal)] += 1
    count = 0
    for val in vent_map.values():
        if val >= 2:
            count += 1
    return count

print(part1())
print(part2())