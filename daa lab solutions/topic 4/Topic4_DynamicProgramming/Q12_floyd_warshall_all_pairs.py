def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)  # undirected
    print("Distance matrix BEFORE:")
    for row in dist:
        print(row)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print("Distance matrix AFTER:")
    for row in dist:
        print(row)
    return dist

def city_within_threshold(n, edges, distanceThreshold):
    dist = floyd_warshall(n, edges)
    best_city, best_count = -1, float('inf')
    for i in range(n):
        count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if count <= best_count:
            best_count = count
            best_city = i
    return best_city

if __name__ == "__main__":
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    print("City:", city_within_threshold(n, edges, 4))  # 3

# --- Bonus: generic directed-edge Floyd-Warshall shortest path between two named nodes ---
def floyd_warshall_directed(nodes, directed_edges, src, dst):
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
    return dist[idx[src]][idx[dst]]

if __name__ == "__main__":
    nodes = ["City1", "City2", "City3", "City4"]
    directed_edges = [
        ("City1","City2",3), ("City1","City3",8), ("City1","City4",-4),
        ("City2","City4",1), ("City2","City3",4),
        ("City3","City1",2), ("City4","City3",-5), ("City4","City2",6),
    ]
    print("City 1 to City 3 =", floyd_warshall_directed(nodes, directed_edges, "City1", "City3"))  # -9
