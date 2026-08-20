def insertion_sort(arr):
    # Stable sort: preserves relative order of equal (duplicate) elements
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

if __name__ == "__main__":
    print(insertion_sort([3,1,4,1,5,9,2,6,5,3]))  # [1,1,2,3,3,4,5,5,6,9]
    print(insertion_sort([5,5,5,5,5]))             # [5,5,5,5,5]
    print(insertion_sort([2,3,1,3,2,1,1,3]))       # [1,1,1,2,2,3,3,3]
