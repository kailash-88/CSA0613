import itertools

def greedy_max_cut(vertices, edges, weights):
    side = {v: 0 for v in vertices}
    for v in vertices:
        gain0 = sum(weights[(u, w)] for (u, w) in edges if v in (u, w)
                    for other in [u if v == w else w] if side[other] == 1)
        # simple greedy: place each vertex on the side that maximizes cut edges so far
        cut_if_0 = sum(weights[e] for e in edges if v in e and side[e[0] if e[1]==v else e[1]] == 1)
        cut_if_1 = sum(weights[e] for e in edges if v in e and side[e[0] if e[1]==v else e[1]] == 0)
        side[v] = 0 if cut_if_0 >= cut_if_1 else 1
    cut_edges = [e for e in edges if side[e[0]] != side[e[1]]]
    weight = sum(weights[e] for e in cut_edges)
    return cut_edges, weight

def exhaustive_max_cut(vertices, edges, weights):
    best_weight = -1
    best_cut = None
    n = len(vertices)
    for bits in itertools.product([0,1], repeat=n):
        side = dict(zip(vertices, bits))
        cut_edges = [e for e in edges if side[e[0]] != side[e[1]]]
        weight = sum(weights[e] for e in cut_edges)
        if weight > best_weight:
            best_weight = weight
            best_cut = cut_edges
    return best_cut, best_weight

if __name__ == "__main__":
    V = [1,2,3,4]
    E = [(1,2),(1,3),(2,3),(2,4),(3,4)]
    W = {(1,2):2, (1,3):1, (2,3):3, (2,4):4, (3,4):2}

    g_cut, g_weight = greedy_max_cut(V, E, W)
    print("Greedy Maximum Cut:", g_cut, "Weight =", g_weight)

    e_cut, e_weight = exhaustive_max_cut(V, E, W)
    print("Optimal Maximum Cut (Exhaustive Search):", e_cut, "Weight =", e_weight)

    print(f"Performance Comparison: Greedy solution achieves {100*g_weight/e_weight:.0f}% of the optimal weight.")
