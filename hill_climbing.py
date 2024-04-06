import random

def generate_random_route(n):
#Here we ar generating a random initial route to visit all places(n) and return a list for a random route.
    route = list(range(n))
    random.shuffle(route)
    return route 

def calculate_total_distance(adjacency_matrix, route):  
#And here we do the calculations for total distance of a route based on the adjacency of matrix and return the total distance of the route.
    total_distance = 0
    for i in range(len(route) - 1):
        current_place = route[i]
        next_place = route[i + 1]
        total_distance += adjacency_matrix[current_place][next_place]
    return total_distance

def explore_neighbors(route):
    #To explore neighboring solutions we swap the order of two random chosen places and return a list of neighboring routes. 
    neighbors = []
    n = len(route)

    for i in range(n):
        for j in range(i + 1, n):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors

def hill_climbing(adjacency_matrix):
    #This is the main function that implements the Hill Cl
    n = len(adjacency_matrix)
    current_route = generate_random_route(n)
    current_distance = calculate_total_distance(adjacency_matrix, current_route)
    explored_routes = [current_route]

    while True:
        neighbors = explore_neighbors(current_route)
        best_neighbor = None
        best_distance = current_distance

        for neighbor in neighbors:
            neighbor_distance = calculate_total_distance(adjacency_matrix, neighbor)
            if neighbor_distance < best_distance:
                best_neighbor = neighbor
                best_distance = neighbor_distance

        if best_neighbor is None:
            break

        current_route = best_neighbor
        current_distance = best_distance
        explored_routes.append(current_route)

    return current_route, current_distance, explored_routes



#usage
adjacency_matrix = [
    [0, 7, 20, 15, 12],
    [7, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]

best_route, best_distance, explored_routes = hill_climbing(adjacency_matrix)
print("Best Route:", best_route)
print("Best Distance:", best_distance)
print("Explored Route:", explored_routes)
