class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst = []
    total = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total

if __name__ == "__main__":
    edges1 = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    print(kruskal(4, edges1))  # total weight 19

    edges2 = [(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]
    print(kruskal(5, edges2))  # total weight 16
