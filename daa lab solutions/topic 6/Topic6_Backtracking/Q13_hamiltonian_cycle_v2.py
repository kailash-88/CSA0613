# Same Hamiltonian-cycle backtracking check as Q12, run on the n=4 example.
def hamiltonian_cycle_exists(n, edges):
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    path = [0]
    visited = [False]*n
    visited[0] = True

    def backtrack():
        if len(path) == n:
            return path[-1] in adj[0]
        for nxt in adj[path[-1]]:
            if not visited[nxt]:
                visited[nxt] = True
                path.append(nxt)
                if backtrack():
                    return True
                path.pop()
                visited[nxt] = False
        return False

    if backtrack():
        return True, path + [0]
    return False, None

if __name__ == "__main__":
    exists, cycle = hamiltonian_cycle_exists(4, [(0,1),(1,2),(2,3),(3,0),(0,2)])
    print("Hamiltonian Cycle Exists:", exists, "Example cycle:", cycle)
