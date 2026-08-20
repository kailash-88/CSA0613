import time

def first_fit(weights, capacity):
    bins = []
    for w in weights:
        placed = False
        for i in range(len(bins)):
            if bins[i] + w <= capacity:
                bins[i] += w
                placed = True
                break
        if not placed:
            bins.append(w)
    return bins

def best_fit(weights, capacity):
    bins = []
    for w in weights:
        best_idx = -1
        best_remaining = capacity + 1
        for i in range(len(bins)):
            remaining = capacity - bins[i]
            if remaining >= w and remaining < best_remaining:
                best_remaining = remaining
                best_idx = i
        if best_idx == -1:
            bins.append(w)
        else:
            bins[best_idx] += w
    return bins

if __name__ == "__main__":
    weights = [4,8,1,4,2,1]
    capacity = 10
    start = time.time()
    bins = first_fit(weights, capacity)
    elapsed = time.time() - start
    print("Number of Bins Used (First-Fit):", len(bins))
    print("Bin loads:", bins)
    print(f"Computational Time: O(n) per item scan; measured {elapsed:.6f}s for n={len(weights)}")

    bins_bf = best_fit(weights, capacity)
    print("Number of Bins Used (Best-Fit):", len(bins_bf))
    print("Bin loads:", bins_bf)
