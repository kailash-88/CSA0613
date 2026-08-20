import itertools

def subset_sum_exists(arr, target):
    n = len(arr)
    A, B = arr[:n//2], arr[n//2:]
    def subset_sums(lst):
        sums = set()
        for r in range(len(lst)+1):
            for combo in itertools.combinations(lst, r):
                sums.add(sum(combo))
        return sums
    sumsA = subset_sums(A)
    sumsB = subset_sums(B)
    sumsB_set = sumsB
    for a in sumsA:
        if (target - a) in sumsB_set:
            return True
    return False

if __name__ == "__main__":
    print(subset_sum_exists([1,3,9,2,7,12], 15))  # True
    print(subset_sum_exists([3,34,4,12,5,2], 15)) # True (3+12? =15 yes)
