import random
import numpy as np
import matplotlib.pyplot as plt
def random_walk(n):
    """Return the coordinates after 'n' random steps."""
    x, y = 0, 0
    for _ in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
    return (x, y)
def distance_from_home(x, y):
    """Return the Manhattan distance from the origin (0,0)."""
    return abs(x) + abs(y)
def monte_carlo_simulation(max_steps, num_simulations):
    """Run the Monte Carlo simulation for a range of step sizes."""
    results = {}
    for steps in range(1, max_steps + 1):
        total_distance = 0
        for _ in range(num_simulations):
            x, y = random_walk(steps)
            total_distance += distance_from_home(x, y)
        average_distance = total_distance / num_simulations
        results[steps] = average_distance
    return results
def find_max_steps(results, max_distance):
    """Find the maximum steps where the average distance is <= max_distance."""
    for steps, avg_distance in results.items():
        if avg_distance > max_distance:
            return steps - 1  # Return the previous step count
    return max(results.keys())  # If all distances are within the limit

# Parameters
max_steps = 100  # The maximum number of steps to simulate
num_simulations = 10000  # The number of simulations to run
max_distance = 4  # The maximum average distance from home

# Run the simulation
results = monte_carlo_simulation(max_steps, num_simulations)

# Find the longest random walk within the desired distance
max_steps_within_distance = find_max_steps(results, max_distance)
print(f"The longest random walk you can take, on average, ending up 4 blocks or fewer from home is: {max_steps_within_distance} steps.")

# Plot the results
steps = list(results.keys())
average_distances = list(results.values())
plt.plot(steps, average_distances, marker='o')
plt.axhline(y=max_distance, color='r', linestyle='--')
plt.xlabel('Number of Steps')
plt.ylabel('Average Distance from Home')
plt.title('Average Distance from Home vs Number of Steps in a Random Walk')
plt.show()