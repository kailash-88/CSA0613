def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    print(f"Partition around pivot {pivot}: {less} [{pivot}] {greater}")
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    print(quick_sort([10,16,8,12,15,6,3,9,5]))
    print(quick_sort([12,4,78,23,45,67,89,1]))
    print(quick_sort([38,27,43,3,9,82,10]))
