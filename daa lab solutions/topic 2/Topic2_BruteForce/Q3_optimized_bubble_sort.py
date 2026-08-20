def bubble_sort_optimized(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:   # stop early if already sorted
            break
    return a

if __name__ == "__main__":
    print(bubble_sort_optimized([64,25,12,22,11]))  # [11,12,22,25,64]
    print(bubble_sort_optimized([29,10,14,37,13]))  # [10,13,14,29,37]
    print(bubble_sort_optimized([3,5,2,1,4]))       # [1,2,3,4,5]
    print(bubble_sort_optimized([1,2,3,4,5]))       # [1,2,3,4,5]
    print(bubble_sort_optimized([5,4,3,2,1]))       # [1,2,3,4,5]
