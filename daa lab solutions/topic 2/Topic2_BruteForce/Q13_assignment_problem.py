import itertools

def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][assignment[i]] for i in range(len(assignment)))

def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    best_cost = float('inf')
    best_assignment = None
    for perm in itertools.permutations(range(n)):
        c = total_cost(perm, cost_matrix)
        if c < best_cost:
            best_cost = c
            best_assignment = perm
    pairs = [(f"worker {i+1}", f"task {best_assignment[i]+1}") for i in range(n)]
    return pairs, best_cost

if __name__ == "__main__":
    cm1 = [[3,10,7],[8,5,12],[4,6,9]]
    print(assignment_problem(cm1))  # cost 19
    cm2 = [[15,9,4],[8,7,18],[6,12,11]]
    print(assignment_problem(cm2))  # cost 24
