def min_max(arr, lo, hi):
    if lo == hi:
        return arr[lo], arr[lo]
    if hi - lo == 1:
        return (arr[lo], arr[hi]) if arr[lo] < arr[hi] else (arr[hi], arr[lo])
    mid = (lo + hi) // 2
    min1, max1 = min_max(arr, lo, mid)
    min2, max2 = min_max(arr, mid+1, hi)
    return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    a = [5,7,3,4,9,12,6,2]
    mn, mx = min_max(a, 0, len(a)-1)
    print(f"Min = {mn}, Max = {mx}")   # Min=2, Max=12
    a2 = [1,3,5,7,9,11,13,15,17]
    mn, mx = min_max(a2, 0, len(a2)-1)
    print(f"Min = {mn}, Max = {mx}")   # Min=1, Max=17
    a3 = [22,34,35,36,43,67,12,13,15,17]
    mn, mx = min_max(a3, 0, len(a3)-1)
    print(f"Min = {mn}, Max = {mx}")   # Min=12, Max=67
