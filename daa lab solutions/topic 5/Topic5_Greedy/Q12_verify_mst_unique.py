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

def kruskal_all_msts_weight(n, edges):
    dsu = DSU(n)
    total = 0
    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total

def is_mst_unique(n, edges, given_mst):
    # An MST is unique iff, for every distinct edge weight cycle formed when
    # adding a non-tree edge, no alternative edge of the SAME weight could
    # replace a tree edge on that cycle. We check by trying each edge not in
    # the given MST and seeing whether it could substitute for a tree edge of
    # equal weight without breaking the tree/increasing total weight.
    mst_set = set((min(u,v), max(u,v), w) for u, v, w in given_mst)
    given_weight = sum(w for _, _, w in given_mst)

    for i in range(len(edges)):
        # try building an MST that excludes edges[i] if it's a tie candidate
        pass

    # Simplest robust check: find ALL edges with weight equal to some tree edge weight,
    # and test if swapping produces an alternative spanning tree of equal weight.
    alt_mst = None
    for skip_idx in range(len(edges)):
        remaining = edges[:skip_idx] + edges[skip_idx+1:]
        dsu = DSU(n)
        total = 0
        count = 0
        chosen = []
        for u, v, w in sorted(remaining, key=lambda e: e[2]):
            if dsu.union(u, v):
                chosen.append((u, v, w))
                total += w
                count += 1
        if count == n - 1 and total == given_weight:
            chosen_set = set((min(u,v), max(u,v), w) for u, v, w in chosen)
            if chosen_set != mst_set:
                alt_mst = chosen
                break
    return alt_mst is None, alt_mst, given_weight

if __name__ == "__main__":
    edges1 = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    given1 = [(2,3,4),(0,3,5),(0,1,10)]
    unique, alt, w = is_mst_unique(4, edges1, given1)
    print("Is the given MST unique?", unique)

    edges2 = [(0,1,1),(0,2,1),(1,3,2),(2,3,2),(3,4,3),(4,2,3)]
    given2 = [(0,1,1),(0,2,1),(1,3,2),(3,4,3)]
    unique2, alt2, w2 = is_mst_unique(5, edges2, given2)
    print("Is the given MST unique?", unique2)
    if not unique2:
        print("Another possible MST:", alt2)
        print("Total weight of MST:", w2)
