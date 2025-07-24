import itertools

# Define cities and ticket price per km
cities = ['A', 'B', 'C', 'D']
ticket_price_per_km = 5
fuel_cost_per_km = 0.5  # Cost of fuel per km

# Set fixed distances between cities (symmetric matrix)
distances = {
    ('A', 'B'): 100, ('A', 'C'): 150, ('A', 'D'): 200,
    ('B', 'C'): 120, ('B', 'D'): 100,
    ('C', 'D'): 130,
    ('B', 'A'): 100, ('C', 'A'): 150, ('D', 'A'): 200,
    ('C', 'B'): 120, ('D', 'B'): 100,
    ('D', 'C'): 130
}

# Print distances between cities
print("Distances between cities:")
for i in cities:
    for j in cities:
        if i != j:
            print(f"{i} to {j}: {distances[(i, j)]} km")

# Set fixed demands between city pairs
demands = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 5,
    ('B', 'C'): 30, ('B', 'D'): 12,
    ('C', 'B'): 6, ('C', 'D'): 10,
    ('B', 'A'): 0, ('C', 'A'): 0, ('D', 'A'): 0,
    ('D', 'B'): 0, ('D', 'C'): 0
}

# Print demands between city pairs
print("\nDemands between city pairs:")
for (i, j), demand in demands.items():
    if i != j:
        print(f"{i} to {j}: {demand} passengers")

# Define function to calculate profit for a given path
def calculate_profit(path):
    profit = 0
    total_fuel_cost = 0
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        distance = distances[(start, end)]
        demand = demands[(start, end)]
        revenue = demand * distance * ticket_price_per_km
        fuel_cost = distance * fuel_cost_per_km
        total_fuel_cost += fuel_cost
        profit += (revenue - fuel_cost)
    return profit

# Generate all valid paths from A to D without revisiting cities
start_city = 'A'
end_city = 'D'
valid_paths = [path for path in itertools.permutations(cities) if path[0] == start_city and path[-1] == end_city]

# Calculate the profit for each path and find the optimal one
optimal_path = None
max_profit = 0
for path in valid_paths:
    profit = calculate_profit(path)
    if profit > max_profit:
        max_profit = profit
        optimal_path = path

# Print the optimal path and profit
print("\nOptimal path and profit:")
print(f"Optimal path: {' -> '.join(optimal_path)}")
print(f"Maximum profit: {max_profit:.2f} rupees")
