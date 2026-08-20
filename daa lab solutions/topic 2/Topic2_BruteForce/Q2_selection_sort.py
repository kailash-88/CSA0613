def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
# Selection Sort: simple to implement (two nested loops, no extra data structures)
# but inefficient for large datasets since it always makes O(n^2) comparisons
# regardless of the initial order of the array.

if __name__ == "__main__":
    print(selection_sort([5,2,9,1,5,6]))   # [1,2,5,5,6,9]
    print(selection_sort([10,8,6,4,2]))    # [2,4,6,8,10]
    print(selection_sort([1,2,3,4,5]))     # [1,2,3,4,5]
