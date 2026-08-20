def binary_search_verbose(arr, key):
    lo, hi = 0, len(arr) - 1
    step = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"Step {step}: lo={lo}, hi={hi}, mid={mid}, arr[mid]={arr[mid]}")
        step += 1
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# If the array were NOT sorted, binary search's logic (discarding half the
# search space based on a comparison with the middle element) would no
# longer be valid, since there is no guarantee about which half the key
# lies in. This would produce incorrect results (false negatives/positives)
# even though it would still run in O(log n) time.

if __name__ == "__main__":
    print("Index:", binary_search_verbose([3,9,14,19,25,31,42,47,53], 31))  # 5
    print("Index:", binary_search_verbose([13,19,24,29,35,41,42], 42))     # 6
    print("Index:", binary_search_verbose([20,40,60,80,100,120], 60))      # 2
