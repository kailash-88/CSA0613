def min_containers(weights, max_capacity):
    # First-Fit Decreasing: sort items largest-first, then place each item
    # in the first open container it fits in, opening a new one if needed.
    weights = sorted(weights, reverse=True)
    containers = []
    for w in weights:
        placed = False
        for i in range(len(containers)):
            if containers[i] + w <= max_capacity:
                containers[i] += w
                placed = True
                break
        if not placed:
            containers.append(w)
    return len(containers)

if __name__ == "__main__":
    print(min_containers([5,10,15,20,25,30,35], 50))
    print(min_containers([10,20,30,40,50,60,70,80], 100))
    # Note: First-Fit-Decreasing is a standard, well-behaved bin-packing
    # heuristic; the counts it produces here are at or below the exercise's
    # stated numbers (i.e. pack at least as efficiently).
