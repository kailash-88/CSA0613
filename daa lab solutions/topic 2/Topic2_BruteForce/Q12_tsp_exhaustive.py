import itertools, math

def distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def tsp(cities):
    start = cities[0]
    rest = cities[1:]
    best_dist = float('inf')
    best_path = None
    for perm in itertools.permutations(rest):
        path = [start] + list(perm) + [start]
        d = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))
        if d < best_dist:
            best_dist = d
            best_path = path
    return best_dist, best_path

if __name__ == "__main__":
    for cities in [[(1,2),(4,5),(7,1),(3,6)], [(2,4),(8,1),(1,7),(6,3),(5,9)]]:
        dist, path = tsp(cities)
        print("Shortest Distance:", dist)
        print("Shortest Path:", path)
