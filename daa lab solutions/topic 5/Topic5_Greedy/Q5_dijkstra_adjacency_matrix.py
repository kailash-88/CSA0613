def dijkstra_matrix(graph, source):
    n = len(graph)
    INF = float('inf')
    dist = [INF]*n
    dist[source] = 0
    visited = [False]*n
    for _ in range(n):
        u = min((d, i) for i, d in enumerate(dist) if not visited[i])[1]
        visited[u] = True
        for v in range(n):
            if graph[u][v] != INF and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    return dist

if __name__ == "__main__":
    INF = float('inf')
    g1 = [[0,10,3,INF,INF],
          [INF,0,1,2,INF],
          [INF,4,0,8,2],
          [INF,INF,INF,0,7],
          [INF,INF,INF,9,0]]
    print(dijkstra_matrix(g1, 0))  # [0,7,3,9,5]

    g2 = [[0,5,INF,10],
          [INF,0,3,INF],
          [INF,INF,0,1],
          [INF,INF,INF,0]]
    print(dijkstra_matrix(g2, 0))  # [0,5,8,9]
