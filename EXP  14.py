from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))  
    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        current_path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            print("Steps to reach the target:")
            for step in current_path:
                print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
            return True

        possible_states = [
            (jug1_capacity, jug2),         
            (jug1, jug2_capacity),         
            (0, jug2),                     
            (jug1, 0),                     
            (0, jug1 + jug2) if jug1 + jug2 <= jug2_capacity else (jug1 - (jug2_capacity - jug2), jug2_capacity),  # Pour Jug1 → Jug2
            (jug1 + jug2, 0) if jug1 + jug2 <= jug1_capacity else (jug1_capacity, jug2 - (jug1_capacity - jug1))   # Pour Jug2 → Jug1
        ]

        for state in possible_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))

    print("No solution.")
    return False

jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_bfs(jug1_capacity, jug2_capacity, target)
