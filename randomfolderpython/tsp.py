# from queue import PriorityQueue

# def tsp_best_first_search(graph):
#     start_node = 'A'
#     visited = {start_node}
#     paths = PriorityQueue()
#     paths.put((0, [start_node]))

#     all_states = []
#     while not paths.empty():
#         cost, path = paths.get()
#         current_node = path[-1]

#         if len(visited) == len(graph):
#             all_states.append((path, cost))
#             return all_states

#         for neighbor, distance in graph[current_node].items():
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 new_cost = cost + distance
#                 new_path = path + [neighbor]
#                 paths.put((new_cost, new_path))

#         all_states.append((path, cost))

#     return None

# # Example usage
# graph = {
#     'A': {'B': 5, 'D': 8},
#     'B': {'A': 5, 'C': 10, 'D': 3, 'E': 9},
#     'C': {'B': 10, 'E': 1},
#     'D': {'A': 8, 'B': 3, 'E': 6},
#     'E': {'B': 9, 'C': 1, 'D': 6, 'F': 2},
#     'F': {'E': 2}
# }

# states = tsp_best_first_search(graph)
# for path, cost in states:
#     print(f'Visited: {path} with cost {cost}')


from queue import PriorityQueue
from typing import Dict, List, Tuple

def tsp_best_first_search(graph: Dict[str, Dict[str, int]], heuristic: Dict[str, int]) -> List[Tuple[List[str], int]]:
    start_node = 'A'
    visited = {start_node}
    paths = PriorityQueue()
    paths.put((heuristic[start_node], [start_node]))

    all_states = []
    while not paths.empty():
        cost, path = paths.get()
        current_node = path[-1]

        if len(visited) == len(graph):
            all_states.append((path, cost))
            return all_states

        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                new_cost = cost + distance
                new_path = path + [neighbor]
                heuristic_val = new_cost + heuristic[neighbor]
                paths.put((heuristic_val, new_path))

        all_states.append((path, cost))

    return None

# Example usage
graph = {
    'A': {'B': 5, 'D': 8},
    'B': {'A': 5, 'C': 10, 'D': 3, 'E': 9},
    'C': {'B': 10, 'E': 1},
    'D': {'A': 8, 'B': 3, 'E': 6},
    'E': {'B': 9, 'C': 1, 'D': 6, 'F': 2},
    'F': {'E': 2}
}

heuristic = {
    'A': 17,
    'B': 11,
    'C': 4,
    'D': 15,
    'E': 6,
    'F': 0
}

states = tsp_best_first_search(graph, heuristic)
for path, cost in states:
    print(f'Visited: {path} with cost {cost}')
