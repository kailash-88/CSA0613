def merge_sort_count(arr):
    comparisons = 0
    def sort(a):
        nonlocal comparisons
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)
    def merge(left, right):
        nonlocal comparisons
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        result.extend(left[i:]); result.extend(right[j:])
        return result
    sorted_arr = sort(arr)
    return sorted_arr, comparisons

if __name__ == "__main__":
    sorted_arr, cmp = merge_sort_count([12,4,78,23,45,67,89,1])
    print(sorted_arr, "Comparisons:", cmp)
    sorted_arr, cmp = merge_sort_count([38,27,43,3,9,82,10])
    print(sorted_arr, "Comparisons:", cmp)
