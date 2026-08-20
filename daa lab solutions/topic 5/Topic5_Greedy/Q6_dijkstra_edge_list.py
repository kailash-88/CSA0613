import heapq
from collections import defaultdict

def dijkstra_edge_list(n, edges, source, target):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # treat edge list as an undirected graph
    dist = [float('inf')]*n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist[target]

if __name__ == "__main__":
    edges1 = [(0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),
              (2,3,11),(2,5,2),(3,4,6),(4,5,9)]
    print(dijkstra_edge_list(6, edges1, 0, 4))  # 20

    edges2 = [(0,1,10),(0,4,3),(1,2,2),(1,4,4),(2,3,9),(3,2,7),
              (4,1,1),(4,2,8),(4,3,2)]
    print(dijkstra_edge_list(5, edges2, 0, 3))
    # Note: 0->4->3 (3+2=5) is a genuinely shorter path than the exercise's
    # stated answer of 8, so this correct Dijkstra run returns 5.
