import math

def closest_pair_brute_force(points):
    n = len(points)
    min_dist = float('inf')
    pair = None
    for i in range(n):
        for j in range(i+1, n):
            d = math.dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

if __name__ == "__main__":
    pts = [(1,2),(4,5),(7,8),(3,1)]
    pair, dist = closest_pair_brute_force(pts)
    print(f"Closest pair: {pair[0]} - {pair[1]}  Minimum distance: {dist}")
