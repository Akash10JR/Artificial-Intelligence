from itertools import permutations

dist = [[0, 10, 15, 20],   
        [10, 0, 35, 25],   
        [15, 35, 0, 30],   
        [20, 25, 30, 0]]   

cities = [0, 1, 2, 3]  

min_path = None
min_cost = float('inf')

for perm in permutations(cities[1:]):
    path = [0] + list(perm) + [0]
    cost = sum(dist[path[i]][path[i+1]] for i in range(len(path) - 1))

    if cost < min_cost:
        min_cost = cost
        min_path = path

city_names = ['A', 'B', 'C', 'D']
print("Shortest Path:", ' → '.join(city_names[i] for i in min_path))
print("Minimum Cost:", min_cost)
