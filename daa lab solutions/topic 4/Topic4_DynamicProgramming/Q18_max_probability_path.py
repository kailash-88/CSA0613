import heapq

def max_probability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]
    for (a, b), p in zip(edges, succProb):
        graph[a].append((b, p))
        graph[b].append((a, p))

    prob = [0.0]*n
    prob[start] = 1.0
    heap = [(-1.0, start)]
    while heap:
        neg_p, node = heapq.heappop(heap)
        p = -neg_p
        if node == end:
            return p
        if p < prob[node]:
            continue
        for nxt, edge_p in graph[node]:
            new_p = p * edge_p
            if new_p > prob[nxt]:
                prob[nxt] = new_p
                heapq.heappush(heap, (-new_p, nxt))
    return 0.0

if __name__ == "__main__":
    print(round(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2), 5))  # 0.25
    print(round(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2), 5))  # 0.3
