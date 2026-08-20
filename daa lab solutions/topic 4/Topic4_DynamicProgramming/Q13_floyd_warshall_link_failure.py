def floyd_warshall(nodes, directed_edges):
    INF = float('inf')
    idx = {name: i for i, name in enumerate(nodes)}
    n = len(nodes)
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in directed_edges:
        dist[idx[u]][idx[v]] = min(dist[idx[u]][idx[v]], w)
        dist[idx[v]][idx[u]] = min(dist[idx[v]][idx[u]], w)  # bidirectional routers
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist, idx

if __name__ == "__main__":
    nodes = ["A","B","C","D","E","F"]
    edges = [("A","B",1), ("A","C",5), ("B","C",2), ("B","D",1),
             ("C","E",3), ("D","E",1), ("D","F",6), ("E","F",2)]
    dist, idx = floyd_warshall(nodes, edges)
    print("Router A to Router F (before failure):", dist[idx["A"]][idx["F"]])

    edges_after = [e for e in edges if not (set(e[:2]) == {"B","D"})]
    dist2, idx2 = floyd_warshall(nodes, edges_after)
    print("Router A to Router F (after B-D link fails):", dist2[idx2["A"]][idx2["F"]])  # 5
