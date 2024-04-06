import numpy as np
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue

class HomeEnvironment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))

    def add_obstacle(self, x, y, size):
        self.grid[y:y+size, x:x+size] = 1 

    def plot_environment(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.grid, cmap='gray', origin='lower')
        plt.title("Home Environment")
        plt.xlabel("X-axis (3 cells per unit)")
        plt.ylabel("Y-axis (3 cells per unit)")
        plt.grid(True)
        plt.show()


class CleaningRobot:
    def __init__(self, environment):
        self.environment = environment
        self.cost_per_movement = 1
        self.turn_penalty = 2

    def cost_function(self, action):
        if action == "move":
            return self.cost_per_movement
        elif action == "turn":
            return self.turn_penalty

    def heuristic(self, current_state, target_state):
        x1, y1 = current_state
        x2, y2 = target_state
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def get_neighbors(self, state):
        x, y = state
        neighbors = []
        possible_movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in possible_movements:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.environment.width and 0 <= new_y < self.environment.height:
                if self.environment.grid[new_y, new_x] == 0:
                    neighbors.append((new_x, new_y))
        return neighbors

    def astar_search(self, start, target):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == target:
                break

            for next in self.get_neighbors(current):
                new_cost = cost_so_far[current] + self.cost_function("move")
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next, target)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from


# Create the environment
width = 20
height = 20
environment = HomeEnvironment(width, height)

# Add obstacles to the environment
environment.add_obstacle(2, 2, 4)
environment.add_obstacle(10, 5, 3)

# Plot the environment
environment.plot_environment()

# Create the cleaning robot
robot = CleaningRobot(environment)

# Test the cost function
move_cost = robot.cost_function("move")
turn_cost = robot.cost_function("turn")
print("Cost of moving: N$", move_cost)
print("Cost of turning: N$", turn_cost)

# Test the heuristic function
current_state = (3, 5)
target_state = (10, 10)
estimated_distance = robot.heuristic(current_state, target_state)
print("Estimated distance to target:", estimated_distance)

# Test the A* search algorithm
start_state = (0, 0)
target_state = (19, 19)
path = robot.astar_search(start_state, target_state)

# Print the path
print("Path from", start_state, "to", target_state)
current_state = target_state
while current_state != start_state:
    print(current_state)
    current_state = path[current_state]
print(start_state)
