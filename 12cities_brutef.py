import itertools
import random

# Define cities and ticket price per km
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'l']
ticket_price_per_km = 5

# Generate random distances between cities for illustration
random.seed(42)  # For reproducibility
distances = {}
demands = {}

# Generate distances and demands between all pairs of cities
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        city1, city2 = cities[i], cities[j]
        distance = random.randint(50, 300)  # Random distance between 50 km and 300 km
        demand1 = random.randint(0, 50)  # Random demand from city1 to city2
        demand2 = random.randint(0, 50)  # Random demand from city2 to city1
        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance
        demands[(city1, city2)] = demand1
        demands[(city2, city1)] = demand2

# Print distances between cities
print("Distances between cities:")
for i in cities:
    for j in cities:
        if i != j:
            print(f"{i} to {j}: {distances[(i, j)]} km")

# Print demands between city pairs
print("\nDemands between city pairs:")
for (i, j), demand in demands.items():
    if i != j:
        print(f"{i} to {j}: {demand} passengers")

# Define function to calculate profit for a given path
def calculate_profit(path):
    profit = 0
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        distance = distances[(start, end)]
        demand = demands[(start, end)]
        revenue = demand * distance * ticket_price_per_km
        profit += revenue
    return profit

# Generate all valid paths from A to D without revisiting cities
start_city = 'A'
end_city = 'D'

# We will generate permutations of the cities in between A and D
cities_without_A_and_D = [city for city in cities if city not in [start_city, end_city]]

valid_paths = []
for path in itertools.permutations(cities_without_A_and_D):
    # Add A at the start and D at the end
    full_path = [start_city] + list(path) + [end_city]
    valid_paths.append(full_path)

# Calculate the profit for each path and find the optimal one
optimal_path = None
max_profit = 0
for path in valid_paths:
    profit = calculate_profit(path)
    if profit > max_profit:
        max_profit = profit
        optimal_path = path

# Check if the optimal path was found before trying to join it
if optimal_path:
    print("\nOptimal path and profit:")
    print(f"Optimal path: {' -> '.join(optimal_path)}")
    print(f"Maximum profit: {max_profit:.2f} rupees")
else:
    print("\nNo valid path found.")
