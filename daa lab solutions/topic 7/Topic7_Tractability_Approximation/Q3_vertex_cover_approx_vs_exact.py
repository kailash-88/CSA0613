import itertools

def approx_vertex_cover(vertices, edges):
    # Classic 2-approximation: repeatedly pick both endpoints of an
    # uncovered edge and remove all edges they touch.
    remaining = set(edges)
    cover = set()
    while remaining:
        u, v = remaining.pop()
        cover.add(u); cover.add(v)
        remaining = {e for e in remaining if u not in e and v not in e}
    return cover

def exact_vertex_cover(vertices, edges):
    for size in range(1, len(vertices)+1):
        for combo in itertools.combinations(vertices, size):
            cover = set(combo)
            if all(u in cover or v in cover for u, v in edges):
                return cover
    return set(vertices)

if __name__ == "__main__":
    V = [1,2,3,4,5]
    E = [(1,2),(1,3),(2,3),(3,4),(4,5)]
    approx = approx_vertex_cover(V, E)
    exact = exact_vertex_cover(V, E)
    print("Approximation Vertex Cover:", approx)
    print("Exact Vertex Cover (Brute-Force):", exact)
    ratio = len(approx) / len(exact)
    print(f"Performance Comparison: Approximation solution is within a factor of {ratio:.2f} of the optimal (guarantee: <=2x optimal).")
