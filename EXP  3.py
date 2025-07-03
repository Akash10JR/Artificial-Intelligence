def alpha_beta(node, depth, alpha, beta, maximizingPlayer, tree):
    if depth == 0 or node not in tree:
        return node 

    if maximizingPlayer:
        max_eval = float('-inf')
        for child in tree[node]:
            eval = alpha_beta(child, depth - 1, alpha, beta, False, tree)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval = alpha_beta(child, depth - 1, alpha, beta, True, tree)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval

game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

result = alpha_beta('A', 3, float('-inf'), float('inf'), True, game_tree)
print("Optimal value:", result)
