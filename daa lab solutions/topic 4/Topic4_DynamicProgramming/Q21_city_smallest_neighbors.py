def find_the_city(n, edges, distanceThreshold):
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    best_city, best_count = -1, float('inf')
    for i in range(n):
        count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if count <= best_count:
            best_count = count
            best_city = i
    return best_city

if __name__ == "__main__":
    print(find_the_city(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))              # 3
    print(find_the_city(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))  # 0
