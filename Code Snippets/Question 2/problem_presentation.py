adjacency_matrix = [
    [0, 7, 20, 15, 12],
    [7, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]

def calculate_total_distance(adjacency_matrix, route):
    total_distance = 0
    n = len(route)
    
    start = route[0]
    current = route[1]
    total_distance += adjacency_matrix[start][current]
    
    for i in range(1, n):
        previous = route[i - 1]
        current = route[i]
        total_distance += adjacency_matrix[previous][current]
    
    last = route[-1]
    total_distance += adjacency_matrix[last][start]
    
    return total_distance


sample_route = [0, 2, 3, 4, 1, 0]  
total_distance = calculate_total_distance(adjacency_matrix, sample_route)
print(f"Total distance for the route {sample_route}: {total_distance}")
