import itertools

def greedy_set_cover(universe, sets):
    universe = set(universe)
    sets = [set(s) for s in sets]
    covered = set()
    chosen = []
    while covered != universe:
        best = max(sets, key=lambda s: len(s - covered))
        if len(best - covered) == 0:
            break
        chosen.append(best)
        covered |= best
    return chosen

def optimal_set_cover(universe, sets):
    universe = set(universe)
    sets = [set(s) for s in sets]
    n = len(sets)
    for size in range(1, n+1):
        for combo in itertools.combinations(range(n), size):
            union = set()
            for i in combo:
                union |= sets[i]
            if union == universe:
                return [sets[i] for i in combo]
    return sets

if __name__ == "__main__":
    U = [1,2,3,4,5,6,7]
    S = [{1,2,3},{2,4},{3,4,5,6},{4,5},{5,6,7},{6,7}]
    greedy = greedy_set_cover(U, S)
    optimal = optimal_set_cover(U, S)
    print("Greedy Set Cover:", greedy, "-> uses", len(greedy), "sets")
    print("Optimal Set Cover:", optimal, "-> uses", len(optimal), "sets")
