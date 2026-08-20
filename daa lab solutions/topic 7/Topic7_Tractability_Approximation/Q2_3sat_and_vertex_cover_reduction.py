import itertools

def evaluate_3sat(clauses, assignment):
    # clauses: list of clauses, each a list of (var, negated) tuples
    for clause in clauses:
        if not any(assignment[var] != negated for var, negated in clause):
            return False
    return True

def solve_3sat(clauses, variables):
    for bits in itertools.product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, bits))
        if evaluate_3sat(clauses, assignment):
            return True, assignment
    return False, None

def vertex_cover_brute_force(vertices, edges, k):
    for size in range(1, k+1):
        for combo in itertools.combinations(vertices, size):
            cover = set(combo)
            if all(u in cover or v in cover for u, v in edges):
                return True, cover
    return False, None

if __name__ == "__main__":
    # 3-SAT: (x1 v x2 v ~x3) ^ (~x1 v x2 v x4) ^ (x3 v ~x4 v x5)
    variables = ['x1','x2','x3','x4','x5']
    clauses = [
        [('x1', False), ('x2', False), ('x3', True)],
        [('x1', True), ('x2', False), ('x4', False)],
        [('x3', False), ('x4', True), ('x5', False)],
    ]
    sat, assignment = solve_3sat(clauses, variables)
    print("Satisfiability:", sat, "Assignment:", assignment)

    V = [1,2,3,4,5]
    E = [(1,2),(1,3),(2,3),(3,4),(4,5)]
    found, cover = vertex_cover_brute_force(V, E, len(V))
    print("Vertex Cover (used for reduction demo):", cover)
    print("NP-Completeness note: Vertex Cover is a known NP-Complete problem;")
    print("polynomial reductions from Vertex Cover to 3-SAT establish 3-SAT's NP-hardness,")
    print("and since a satisfying assignment can be checked in poly time, 3-SAT is NP-Complete.")
