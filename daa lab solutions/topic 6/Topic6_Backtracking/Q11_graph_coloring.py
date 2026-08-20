def graph_coloring_max_regions_you_color(n, edges, k):
    # Simplified simulation: players color in turn order (You, Alice, Bob),
    # each picks any valid uncolored region + color respecting adjacency
    # constraints, using backtracking to explore best outcome for "you".
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)

    colors = [-1]*n

    def valid_colors(region):
        used = {colors[nb] for nb in adj[region] if colors[nb] != -1}
        return [c for c in range(k) if c not in used]

    def backtrack(turn, remaining):
        if not remaining:
            return 0
        best = 0
        player = turn % 3  # 0=you, 1=Alice, 2=Bob
        for region in list(remaining):
            vc = valid_colors(region)
            if not vc:
                continue
            for c in vc:
                colors[region] = c
                remaining.remove(region)
                score = backtrack(turn+1, remaining) + (1 if player == 0 else 0)
                remaining.add(region)
                colors[region] = -1
                best = max(best, score)
        if best == 0 and remaining:
            # no assignable region found for anyone; stop
            return 0
        return best

    return backtrack(0, set(range(n)))

def min_colors_graph_coloring(n, edges):
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    colors = [-1]*n

    def is_valid(node, c):
        return all(colors[nb] != c for nb in adj[node])

    def backtrack(node, k):
        if node == n:
            return True
        for c in range(k):
            if is_valid(node, c):
                colors[node] = c
                if backtrack(node+1, k):
                    return True
                colors[node] = -1
        return False

    for k in range(1, n+1):
        colors[:] = [-1]*n
        if backtrack(0, k):
            return k, colors[:]
    return n, colors

if __name__ == "__main__":
    n, edges, k = 4, [(0,1),(1,2),(2,3),(3,0),(0,2)], 3
    print("Maximum number of regions you can color:", graph_coloring_max_regions_you_color(n, edges, k))

    min_k, coloring = min_colors_graph_coloring(4, [(0,1),(1,2),(2,3),(3,0),(0,2)])
    print("Minimum colors needed:", min_k, "Coloring:", coloring)
