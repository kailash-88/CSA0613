import math

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull_brute_force(points):
    n = len(points)
    hull_points = set()
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
                hull_points.add(points[i])
                hull_points.add(points[j])
    cx = sum(p[0] for p in hull_points) / len(hull_points)
    cy = sum(p[1] for p in hull_points) / len(hull_points)
    ordered = sorted(hull_points, key=lambda p: math.atan2(p[1]-cy, p[0]-cx))
    return ordered

if __name__ == "__main__":
    pts = [(1,1),(4,6),(8,1),(0,0),(3,3)]
    print("Convex Hull:", convex_hull_brute_force(pts))  # [(0,0),(1,1)? or similar ccw order]
