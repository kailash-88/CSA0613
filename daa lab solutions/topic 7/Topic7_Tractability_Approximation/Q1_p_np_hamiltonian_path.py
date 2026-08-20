# Hamiltonian Path is NP: given a candidate path (certificate), verification
# runs in polynomial time. Finding one in general graphs has no known
# polynomial algorithm, but for this small instance we can search directly.
def hamiltonian_path_exists(vertices, edges):
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)

    n = len(vertices)
    for start in vertices:
        path = [start]
        visited = {start}

        def backtrack():
            if len(path) == n:
                return True
            for nxt in adj[path[-1]]:
                if nxt not in visited:
                    visited.add(nxt)
                    path.append(nxt)
                    if backtrack():
                        return True
                    path.pop()
                    visited.remove(nxt)
            return False

        if backtrack():
            return True, path[:]
    return False, None

def verify_hamiltonian_path(vertices, edges, path):
    # Polynomial-time (O(n)) verification given a certificate path -- NP witness check
    if sorted(path) != sorted(vertices) or len(set(path)) != len(vertices):
        return False
    edge_set = set()
    for u, v in edges:
        edge_set.add((u, v)); edge_set.add((v, u))
    return all((path[i], path[i+1]) in edge_set for i in range(len(path)-1))

if __name__ == "__main__":
    V = ['A','B','C','D']
    E = [('A','B'),('B','C'),('C','D'),('D','A')]
    exists, path = hamiltonian_path_exists(V, E)
    print("Hamiltonian Path Exists:", exists, "Path:", ' -> '.join(path) if path else None)
    print("Verification (certificate check, P-time):", verify_hamiltonian_path(V, E, path))
