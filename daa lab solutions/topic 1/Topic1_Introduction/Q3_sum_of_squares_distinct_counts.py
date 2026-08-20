def sum_counts(nums):
    n = len(nums)
    total = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(nums[j])
            total += len(seen) ** 2
    return total

if __name__ == "__main__":
    print(sum_counts([1,2,1]))  # 15
    print(sum_counts([1,1]))    # 3
