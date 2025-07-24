# 🚌 Tourist Bus Agency Profit Optimization 📈

## Overview  
This project explores optimization techniques to **maximize profits for a tourist bus agency** by improving route planning and pricing strategy. The approach uses **Linear Programming (LP)** and a **Genetic Algorithm (GA)** to address inefficiencies like underutilized buses, poorly planned routes, and operational costs.

---

## 🔑 Key Features

### 🔍 Problem Focus
- Inefficient route planning
- Underutilization of buses
- High fuel and operational expenses
- Unbalanced demand distribution across cities

### ⚙️ Assumptions
- No bus capacity constraints (all customer demands are satisfied)
- Only fuel cost considered (maintenance costs ignored)
- Buses don’t return to previously visited cities (no backtracking)

### 📐 Methodology
- **Linear Programming (LP)** used for initial route & pricing setup
- **Distance-based pricing** for simplicity
- **Genetic Algorithm (GA)** for optimal path and profit maximization:
  - **Initialization**: Random population of routes
  - **Selection**: Tournament selection of fittest individuals
  - **Crossover**: Inherit characteristics from parent routes
  - **Mutation**: Introduce randomness to avoid local minima
  - **Iteration**: Repeat for fixed generations
  - **Evaluation**: Track the most profitable route

---

## 🧪 Test Scenarios

### ✅ 4 Cities
- Brute-force approach used to enumerate all possibilities
- Comparison with GA results to validate correctness

### 🌍 12 Cities
- Randomly assigned **distances and demands**
- GA used to handle computational complexity
- Output shows profit-maximizing tour among 12 nodes

---

## 🧱 Project Structure

```
tourist-bus-optimizer/
│
├── data/ # Distance and demand matrices
│ └── city_data.json
│
├── algorithms/ # Optimization logic
│ ├── linear_programming.py
│ ├── genetic_algorithm.py
│ └── brute_force.py
│
├── visualizations/ # Route plots and result comparisons
│ ├── routes_4cities.png
│ └── output_12cities.png
│
└── report/ # Final documentation
└── optimization_report.pdf
```

---

## 👥 Contributors

- **Harshal Rudraksha** – Roll No: 230002061  
- **Vansh Raj Singh** – Roll No: 230002079  
- **Vansh Sabharwal** – Roll No: 230002080  

🎓 *Course Project – Optimization and Algorithms*

---

## 🙏 Acknowledgments

- **Python libraries**: `itertools`, `random`, etc.  
- **Genetic Algorithm inspiration**: From optimization toolkits and research examples  
- **Faculty support** – For problem statement and evaluation guidance

---

## 📝 Notes

> 📌 *This project demonstrates how optimization can address logistical inefficiencies in transport businesses. Genetic algorithms provided scalable performance for large instances like the 12-city case.*

---

