def floyd_warshall(nodes, directed_edges):
    INF = float('inf')
    idx = {name: i for i, name in enumerate(nodes)}
    n = len(nodes)
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in directed_edges:
        dist[idx[u]][idx[v]] = min(dist[idx[u]][idx[v]], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist, idx

if __name__ == "__main__":
    # part a: C -> A shortest path
    nodesA = ["A","B","C","D"]
    edgesA = [("B","A",2), ("A","C",3), ("C","D",1), ("D","A",6), ("C","B",7)]
    distA, idxA = floyd_warshall(nodesA, edgesA)
    print("C to A =", distA[idxA["C"]][idxA["A"]])  # 7 (C->B->A = 7+2=9, C->D->A=1+6=7) -> 7

    # part b: E -> C shortest path
    nodesB = ["A","B","C","D","E"]
    edgesB = [("C","A",2), ("A","B",4), ("B","C",1), ("B","E",6), ("E","A",1),
              ("A","D",5), ("D","E",2), ("E","D",4), ("D","C",1), ("C","D",3)]
    distB, idxB = floyd_warshall(nodesB, edgesB)
    print("E to C =", distB[idxB["E"]][idxB["C"]])  # 5
