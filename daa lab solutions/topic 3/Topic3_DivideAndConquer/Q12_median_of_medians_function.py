def median_of_medians(arr, k):
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
    return select(arr, k-1)

if __name__ == "__main__":
    print(median_of_medians([1,2,3,4,5,6,7,8,9,10], 6))          # 6
    print(median_of_medians([23,17,31,44,55,21,20,18,19,27], 5)) # 5th smallest
