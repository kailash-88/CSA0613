import itertools

def meet_in_middle_closest(arr, target):
    n = len(arr)
    A, B = arr[:n//2], arr[n//2:]
    def subset_sums(lst):
        sums = []
        for r in range(len(lst)+1):
            for combo in itertools.combinations(lst, r):
                sums.append(sum(combo))
        return sorted(sums)
    sumsA = subset_sums(A)
    sumsB = subset_sums(B)
    best = None
    best_diff = float('inf')
    for a in sumsA:
        for b in sumsB:
            diff = abs((a+b) - target)
            if diff < best_diff:
                best_diff = diff
                best = a + b
    return best

if __name__ == "__main__":
    print(meet_in_middle_closest([45,34,4,12,5,2], 42))  # closest sum to 42
    print(meet_in_middle_closest([1,3,2,7,4,6], 10))     # closest sum to 10
