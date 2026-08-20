def binary_search_count(arr, key):
    lo, hi = 0, len(arr)-1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comparisons

if __name__ == "__main__":
    print(binary_search_count([5,10,15,20,25,30,35,40,45], 20))  # (3, comparisons) index 3
    print(binary_search_count([10,20,30,40,50,60], 50))
    print(binary_search_count([21,32,40,54,65,76,87], 32))
