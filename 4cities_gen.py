import random

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

# Set fixed demands between city pairs
demands = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 5,
    ('B', 'C'): 30, ('B', 'D'): 12,
    ('C', 'B'): 6, ('C', 'D'): 10,
    ('B', 'A'): 0, ('C', 'A'): 0, ('D', 'A'): 0,
    ('D', 'B'): 0, ('D', 'C'): 0
}

# Function to calculate profit for a given path
def calculate_profit(path):
    profit = 0
    total_fuel_cost = 0
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        distance = distances.get((start, end), float('inf'))
        demand = demands.get((start, end), 0)
        revenue = demand * distance * ticket_price_per_km
        fuel_cost = distance * fuel_cost_per_km
        total_fuel_cost += fuel_cost
        profit += (revenue - fuel_cost)
    return profit

# Generate a random path
start_city = 'A'
end_city = 'D'
def generate_random_path():
    middle_cities = cities[1:-1]  # Exclude start and end cities
    random.shuffle(middle_cities)
    return [start_city] + middle_cities + [end_city]

# Genetic Algorithm Parameters
population_size = 100
generations = 200
mutation_rate = 0.1

# Initialize population
population = [generate_random_path() for _ in range(population_size)]

# Genetic Algorithm
for generation in range(generations):
    # Calculate fitness for each path
    fitness_scores = [(path, calculate_profit(path)) for path in population]
    fitness_scores.sort(key=lambda x: x[1], reverse=True)

    # Selection: take the top 50% paths
    selected_paths = [path for path, _ in fitness_scores[:population_size // 2]]

    # Crossover: create new paths from selected ones
    offspring = []
    while len(offspring) < population_size // 2:
        parent1, parent2 = random.sample(selected_paths, 2)
        cut = random.randint(1, len(cities) - 2)
        child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
        offspring.append(child)

    # Mutation: randomly swap cities in paths
    for path in offspring:
        if random.random() < mutation_rate:
           
            i, j = random.sample(range(1, len(cities) - 1), 2)
            path[i], path[j] = path[j], path[i]

    # Update population
    population = selected_paths + offspring

# Get the best path
best_path = max(population, key=calculate_profit)
max_profit = calculate_profit(best_path)

# Print the optimal path and profit
print("\nOptimal path and profit:")
print(f"Optimal path: {' -> '.join(best_path)}")
print(f"Maximum profit: {max_profit:.2f} rupees")
