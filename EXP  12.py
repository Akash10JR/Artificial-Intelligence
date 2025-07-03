from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    m_left, c_left, boat, path = state
    successors = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for m, c in moves:
        if boat == 1:  
            new_state = (m_left - m, c_left - c, 0, path + [state])
            m_right = 3 - new_state[0]
            c_right = 3 - new_state[1]
        else:  
            new_state = (m_left + m, c_left + c, 1, path + [state])
            m_right = 3 - new_state[0]
            c_right = 3 - new_state[1]

        if is_valid(new_state[0], new_state[1], m_right, c_right):
            successors.append(new_state)
    return successors

def solve():
    initial_state = (3, 3, 1, [])
    goal_state = (0, 0, 0)
    visited = set()
    queue = deque([initial_state])

    while queue:
        current = queue.popleft()
        m_left, c_left, boat, path = current
        if (m_left, c_left, boat) == goal_state:
            full_path = path + [current]
            print("Solution found in", len(full_path) - 1, "moves:\n")
            for i, step in enumerate(full_path):
                print(f"Step {i}: Left({step[0]}M, {step[1]}C), Boat: {'Left' if step[2] == 1 else 'Right'}")
            return

        visited.add((m_left, c_left, boat))
        for state in get_successors(current):
            if (state[0], state[1], state[2]) not in visited:
                queue.append(state)

    print("No solution found.")


solve()
