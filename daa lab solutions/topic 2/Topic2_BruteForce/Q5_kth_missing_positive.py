def find_kth_positive(arr, k):
    for num in arr:
        pass
    missing_before = lambda idx: arr[idx] - (idx + 1)
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if missing_before(mid) < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo + k

if __name__ == "__main__":
    print(find_kth_positive([2,3,4,7,11], 5))  # 9
    print(find_kth_positive([1,2,3,4], 2))     # 6
