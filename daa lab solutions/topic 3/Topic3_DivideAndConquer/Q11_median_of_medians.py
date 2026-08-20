def median_of_medians_select(arr, k):
    # returns the k-th smallest (1-indexed) element using median-of-medians
    # for worst-case O(n) pivot selection.
    def select(lst, k):
        if len(lst) <= 5:
            return sorted(lst)[k]
        chunks = [lst[i:i+5] for i in range(0, len(lst), 5)]
        medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
        pivot = select(medians, len(medians)//2)
        low = [x for x in lst if x < pivot]
        high = [x for x in lst if x > pivot]
        pivots = [x for x in lst if x == pivot]
        if k < len(low):
            return select(low, k)
        elif k < len(low) + len(pivots):
            return pivot
        else:
            return select(high, k - len(low) - len(pivots))
    return select(arr, k-1)  # convert to 0-indexed

if __name__ == "__main__":
    print(median_of_medians_select([12,3,5,7,19], 2))            # 5
    print(median_of_medians_select([12,3,5,7,4,19,26], 3))       # 5
    print(median_of_medians_select([1,2,3,4,5,6,7,8,9,10], 6))   # 6
