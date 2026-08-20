import heapq

def network_delay_time(times, n, k):
    graph = {}
    for u, v, w in times:
        graph.setdefault(u, []).append((v, w))

    dist = {i: float('inf') for i in range(1, n+1)}
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, w in graph.get(node, []):
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1

if __name__ == "__main__":
    print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
    print(network_delay_time([[1,2,1]], 2, 1))                   # 1
    print(network_delay_time([[1,2,1]], 2, 2))                   # -1
