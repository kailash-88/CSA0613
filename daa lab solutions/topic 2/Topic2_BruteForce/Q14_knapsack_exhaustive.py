import itertools

def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

def knapsack_exhaustive(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_selection = []
    for r in range(n+1):
        for combo in itertools.combinations(range(n), r):
            if is_feasible(combo, weights, capacity):
                v = total_value(combo, values)
                if v > best_value:
                    best_value = v
                    best_selection = list(combo)
    return best_selection, best_value

if __name__ == "__main__":
    print(knapsack_exhaustive([2,3,1], [4,5,3], 4))       # ([0,2], 7)
    print(knapsack_exhaustive([1,2,3,4], [2,4,6,3], 6))   # ([0,1,2], 10)
