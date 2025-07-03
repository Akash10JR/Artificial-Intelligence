adjacency = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Green', 'Blue']

def is_valid(region, color, assignment):
    for neighbor in adjacency[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(adjacency):
        return assignment

    unassigned = [r for r in adjacency if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]  

    return None

solution = backtrack({})
if solution:
    for region in sorted(solution):
        print(f"{region}: {solution[region]}")
else:
    print("No solution found.")
