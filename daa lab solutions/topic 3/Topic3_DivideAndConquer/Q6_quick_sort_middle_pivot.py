def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_idx = len(arr) // 2
    pivot = arr[mid_idx]
    rest = arr[:mid_idx] + arr[mid_idx+1:]
    less = [x for x in rest if x < pivot]
    greater = [x for x in rest if x >= pivot]
    print(f"Partition around pivot {pivot}: {less} [{pivot}] {greater}")
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    print(quick_sort([19,72,35,46,58,91,22,31]))
    print(quick_sort([31,23,35,27,11,21,15,28]))
    print(quick_sort([22,34,25,36,43,67,52,13,65,17]))
