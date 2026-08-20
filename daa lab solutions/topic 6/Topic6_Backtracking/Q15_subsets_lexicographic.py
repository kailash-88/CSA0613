def subsets_lexicographic(nums):
    nums = sorted(nums)
    result = []
    path = []

    def backtrack(start):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1)
            path.pop()

    backtrack(0)
    return result
# Handling duplicates: if nums contains duplicates (e.g. [1,2,2]), this
# generator would emit duplicate subsets. To avoid that, skip an index i
# when nums[i] == nums[i-1] and i > start (see Q16 below for the power-set
# variant, which assumes distinct elements as required by the prompt).

if __name__ == "__main__":
    print(subsets_lexicographic([1,2,3]))
    # [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
