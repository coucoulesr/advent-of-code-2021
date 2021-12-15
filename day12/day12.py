from collections import defaultdict

def count_paths(graph, origin='start', seen=set()):   
    """Returns the number of paths through the given graph."""
    if origin == 'end': 
        return 1
    if origin in seen: return 0
    if origin.islower(): seen.add(origin)
    path_count = 0
    for next_hop in graph[origin]:
        path_count += count_paths(graph, next_hop, seen.copy())
    return path_count

def count_paths_revisit(graph, origin='start', seen=set(), revisited=False):
    """
    Returns the number of paths through the given graph with a single revisit
    to a lowercase node that is not start or end allowed.
    """
    if origin == 'end': return 1
    if origin in seen: 
        if origin in ('start', 'end') or revisited:
            return 0
        revisited = True
    if origin.islower(): seen.add(origin)
    path_count = 0
    for next_hop in graph[origin]:
        path_count += \
            count_paths_revisit(graph, next_hop, seen.copy(), revisited)
    return path_count

def part1():
    graph = defaultdict(list)
    with open('example12', 'r') as f:
        for line in f:
            origin, endpoint = [val.strip() for val in line.split('-')]
            graph[origin].append(endpoint)
            graph[endpoint].append(origin)
    return count_paths(graph)

def part2():
    graph = defaultdict(list)
    with open('input12', 'r') as f:
        for line in f:
            origin, endpoint = [val.strip() for val in line.split('-')]
            graph[origin].append(endpoint)
            graph[endpoint].append(origin)
    return count_paths_revisit(graph)

print(part1())
print(part2())