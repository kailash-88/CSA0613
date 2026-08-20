import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair_brute_force(points):
    n = len(points)
    min_dist = float('inf')
    pair = None
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist
# Time complexity: O(n^2) since every pair of points is compared.

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull_brute_force(points):
    # A point is on the hull if all other points lie on one side of the line
    # through every pair of points -- classic O(n^3) brute force.
    n = len(points)
    hull_edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            left = right = False
            valid = True
            for k in range(n):
                if k == i or k == j:
                    continue
                c = cross(points[i], points[j], points[k])
                if c > 0:
                    left = True
                elif c < 0:
                    right = True
                if left and right:
                    valid = False
                    break
            if valid:
                hull_edges.append((points[i], points[j]))
    hull_points = set()
    for a, b in hull_edges:
        hull_points.add(a)
        hull_points.add(b)
    # order points counter-clockwise around centroid
    cx = sum(p[0] for p in hull_points) / len(hull_points)
    cy = sum(p[1] for p in hull_points) / len(hull_points)
    ordered = sorted(hull_points, key=lambda p: math.atan2(p[1]-cy, p[0]-cx))
    return ordered
# Handling collinear points: when multiple points lie on the same edge line,
# only keep the two extreme (endpoint) points on that edge and treat the
# strictly-between points as interior (not part of the hull), or allow c == 0
# to be treated as "on the line" and exclude interior collinear points based
# on distance from the two extremes.

if __name__ == "__main__":
    pts = [(1,2),(4,5),(7,8),(3,1)]
    pair, dist = closest_pair_brute_force(pts)
    print("Closest pair:", pair, "Minimum distance:", dist)

    S = [(10,0),(11,5),(5,3),(9,3.5),(15,3),(12.5,7),(6,6.5),(7.5,4.5)]
    print("Convex Hull:", convex_hull_brute_force(S))
