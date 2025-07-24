import random
import itertools

# Define cities and ticket price per km
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
ticket_price_per_km = 5

# Generate random distances between cities for illustration
random.seed(42)  # For reproducibility
distances = {}
demands = {}

# Generate distances and directional demands between all pairs of cities
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        city1, city2 = cities[i], cities[j]
        distance = random.randint(50, 300)  # Random distance between 50 km and 300 km
        
        # Generate independent demands for each direction
        demand_1_to_2 = random.randint(0, 50)  # Random demand between city1 to city2
        demand_2_to_1 = random.randint(0, 50)  # Random demand between city2 to city1

        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance
        demands[(city1, city2)] = demand_1_to_2
        demands[(city2, city1)] = demand_2_to_1

# Print distances between cities
print("Distances between cities:")
for i in cities:
    for j in cities:
        if i != j:
            print(f"{i} to {j}: {distances[(i, j)]} km")

# Print directional demands between city pairs
print("\nDemands between city pairs:")
for (i, j), demand in demands.items():
    if i != j:
        print(f"{i} to {j}: {demand} passengers")

# Define function to calculate profit for a given path
def calculate_profit(path):
    profit = 0
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        if start != end:  # Ensure no self-loops (e.g., B -> B)
            distance = distances[(start, end)]
            demand = demands[(start, end)]
            revenue = demand * distance * ticket_price_per_km
            profit += revenue
    return profit

# Generate initial population: each individual is a permutation of cities except 'A' and 'D'
def generate_initial_population(pop_size):
    population = []
    cities_without_A_and_D = [city for city in cities if city not in ['A', 'D']]
    
    for _ in range(pop_size):
        random.shuffle(cities_without_A_and_D)
        individual = ['A'] + cities_without_A_and_D + ['D']
        population.append(individual)
    
    return population

# Tournament selection to choose parents
def tournament_selection(population, tournament_size=3):
    selected = random.sample(population, tournament_size)
    selected = sorted(selected, key=calculate_profit, reverse=True)
    return selected[0]  # Return the best individual

# One-point crossover between two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:-1]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:-1]
    
    # Ensure offspring has no repeated cities
    offspring1 = list(dict.fromkeys(offspring1))  # Remove duplicates while preserving order
    offspring2 = list(dict.fromkeys(offspring2))
    
    # Fix the offspring to ensure they have 'A' at the start and 'D' at the end
    if offspring1[0] != 'A': 
        offspring1.insert(0, 'A')
    if offspring1[-1] != 'D': 
        offspring1.append('D')

    if offspring2[0] != 'A': 
        offspring2.insert(0, 'A')
    if offspring2[-1] != 'D': 
        offspring2.append('D')
    
    return offspring1, offspring2

# Mutation: swap two cities in the intermediate part of the route
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        # Only swap cities in the middle part (between A and D)
        idx1 = random.randint(1, len(individual) - 2)
        idx2 = random.randint(1, len(individual) - 2)
        # Swap only if it's a valid swap (i.e., no repeats)
        if idx1 != idx2:
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm to find optimal route
def genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.1):
    population = generate_initial_population(pop_size)
    
    best_route = None
    best_profit = 0
    
    for gen in range(generations):
        new_population = []
        
        # Selection, Crossover, and Mutation
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.append(mutate(offspring1, mutation_rate))
            new_population.append(mutate(offspring2, mutation_rate))
        
        # Evaluate fitness of new population
        population = sorted(new_population, key=calculate_profit, reverse=True)
        
        # Track the best solution
        best_individual = population[0]
        best_individual_profit = calculate_profit(best_individual)
        if best_individual_profit > best_profit:
            best_route = best_individual
            best_profit = best_individual_profit
            
        # Print progress every 100 generations
        if gen % 100 == 0:
            print(f"Generation {gen}, Best Profit: {best_profit:.2f}")
    
    return best_route, best_profit

# Run the genetic algorithm
optimal_route, max_profit = genetic_algorithm(pop_size=100, generations=1000)

# Print the optimal path and profit
print("\nOptimal path and profit:")
print(f"Optimal path: {' -> '.join(optimal_route)}")
print(f"Maximum profit: {max_profit:.2f} rupees")
