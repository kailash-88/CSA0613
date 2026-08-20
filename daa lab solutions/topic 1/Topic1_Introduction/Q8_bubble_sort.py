def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
# Time complexity: O(n^2) worst/average case, O(n) best case (with early-stop variant, see Topic2 Q3)

if __name__ == "__main__":
    print(bubble_sort([5,1,4,2,8]))
