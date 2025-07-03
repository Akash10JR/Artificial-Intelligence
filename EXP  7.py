import heapq

def a_star(graph, start, goal, h):
    open_list = [(h[start], 0, start, [])]
    visited = set()

    while open_list:
        est_total, cost, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        path = path + [node]

        if node == goal:
            return path, cost

        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(open_list, (
                    cost + weight + h[neighbor],  
                    cost + weight,                
                    neighbor,
                    path
                ))
    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 7)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 10, 'B': 8, 'C': 5,
    'D': 7, 'E': 3, 'F': 3,
    'G': 0
}

path, cost = a_star(graph, 'A', 'G', h)
print("Shortest path:", " → ".join(path))
print("Total cost:", cost)
