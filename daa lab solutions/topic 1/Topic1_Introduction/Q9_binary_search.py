def binary_search(arr, key):
    # arr must be sorted for binary search; sort first if needed
    sorted_arr = sorted(arr)
    lo, hi = 0, len(sorted_arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] == key:
            return mid
        elif sorted_arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Time complexity: O(log n)

if __name__ == "__main__":
    X = [3,4,6,-9,10,8,9,30]
    key = 10
    idx = binary_search(X, key)
    print(f"Element {key} is found at position {idx}" if idx != -1 else f"Element {key} is not found")
    key = 100
    idx = binary_search(X, key)
    print(f"Element {key} is found at position {idx}" if idx != -1 else f"Element {key} is not found")
