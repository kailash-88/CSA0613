import itertools

def tsp_held_karp(dist, n):
    # dist is n x n matrix, cities indexed 0..n-1, start at 0
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dist[0][k], 0)
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for b in subset:
                bits |= 1 << b
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k:
                        continue
                    res.append((C[(prev_bits, m)][0] + dist[m][k], m))
                C[(bits, k)] = min(res)
    bits = (1 << n) - 2
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dist[k][0], k))
    return min(res)[0]

if __name__ == "__main__":
    cities = ['A','B','C','D','E']
    dist = {
        ('A','B'):10, ('A','C'):15, ('A','D'):20, ('A','E'):25,
        ('B','C'):35, ('B','D'):25, ('B','E'):30,
        ('C','D'):30, ('C','E'):20,
        ('D','E'):15,
    }
    n = len(cities)
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                a, b = cities[i], cities[j]
                M[i][j] = dist.get((a,b)) or dist.get((b,a))
    print("Shortest total distance:", tsp_held_karp(M, n))
