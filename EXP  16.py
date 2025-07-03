import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

def matrix_to_tuple(matrix):
    return tuple(tuple(row) for row in matrix)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(start_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_list:
        est_cost, cost, current_state, path = heapq.heappop(open_list)

        if current_state == goal_state:
            return path + [current_state]

        visited.add(matrix_to_tuple(current_state))

        for neighbor in get_neighbors(current_state):
            if matrix_to_tuple(neighbor) not in visited:
                new_path = path + [current_state]
                heapq.heappush(open_list, (
                    cost + 1 + manhattan_distance(neighbor),
                    cost + 1,
                    neighbor,
                    new_path
                ))

    return None

def print_path(path):
    for step, state in enumerate(path):
        print(f"\nStep {step}:")
        for row in state:
            print(row)

start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = solve_puzzle(start_state)
if solution:
    print_path(solution)
else:
    print("No solution found.")
