import heapq

def k_closest(points, k):
    heap = [(-(x*x+y*y), [x,y]) for x, y in points]
    # use nlargest-negative trick via nsmallest on distance
    heap = sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
    return heap

if __name__ == "__main__":
    print(k_closest([[1,3],[-2,2],[5,8],[0,1]], 2))  # [[-2,2],[0,1]] (order may vary)
    print(k_closest([[1,3],[-2,2]], 1))               # [[-2,2]]
    print(k_closest([[3,3],[5,-1],[-2,4]], 2))         # [[3,3],[-2,4]]
