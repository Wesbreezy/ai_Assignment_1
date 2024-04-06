import numpy as np
from scipy.optimize import minimize

class TravellingSalesmanSolver:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

    def calculate_distance(self, route):
        total_distance = 0
        num_places = len(route)
        for i in range(num_places - 1):
            from_place = int(route[i])
            to_place = int(route[i + 1])
            total_distance += self.adjacency_matrix[from_place][to_place]
        return total_distance

def hill_climbing(adjacency_matrix, num_iterations):
    num_places = len(adjacency_matrix)
    current_route = np.random.permutation(num_places)
    solver = TravellingSalesmanSolver(adjacency_matrix)
    current_distance = solver.calculate_distance(current_route)

    for _ in range(num_iterations):
        neighbors = []
        for i in range(num_places - 1):
            for j in range(i + 1, num_places):
                neighbor_route = np.copy(current_route)
                neighbor_route[i], neighbor_route[j] = neighbor_route[j], neighbor_route[i]
                neighbors.append(neighbor_route)

        best_neighbor_distance = float('inf')
        best_neighbor_route = None
        for neighbor_route in neighbors:
            neighbor_distance = solver.calculate_distance(neighbor_route)
            if neighbor_distance < best_neighbor_distance:
                best_neighbor_distance = neighbor_distance
                best_neighbor_route = neighbor_route

        if best_neighbor_distance < current_distance:
            current_distance = best_neighbor_distance
            current_route = best_neighbor_route
        else:
            break

    return current_route, current_distance

# Example usage
adjacency_matrix = [
     [0, 7, 20, 15, 12],
    [7, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]

# Calculate the optimal distance using scipy.optimize.minimize
solver = TravellingSalesmanSolver(adjacency_matrix)

# Define the objective function for minimizing the distance
def objective_function(route):
    return solver.calculate_distance(route)

# Define the bounds for each place index
bounds = [(0, len(adjacency_matrix) - 1)] * len(adjacency_matrix)

# Set the starting point for the optimization
x0 = np.arange(len(adjacency_matrix))

# Minimize the objective function
res = minimize(objective_function, x0, method='L-BFGS-B', bounds=bounds)
optimal_distance = res.fun
optimal_route = res.x.astype(int)

print("Optimal Route:", optimal_route)
print("Optimal Distance:", optimal_distance)
print()

# Comparing the distances
num_iterations_list = [100, 500, 1000, 2000, 5000]
for num_iterations in num_iterations_list:
    best_route, best_distance = hill_climbing(adjacency_matrix, num_iterations)
    print("Number of Iterations:", num_iterations)
    print("Best Route (Hill Climbing):", best_route)
    print("Best Distance (Hill Climbing):", best_distance)
    print("Difference from Optimal (Hill Climbing):", best_distance - optimal_distance)
    print("*****")