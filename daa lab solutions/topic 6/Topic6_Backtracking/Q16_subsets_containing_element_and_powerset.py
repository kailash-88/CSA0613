def subsets_containing(nums, x):
    result = []
    n = len(nums)
    others = [v for v in nums if v != x]

    def backtrack(start, path):
        if x in path:
            result.append(sorted(path, key=lambda v: nums.index(v)))
        for i in range(start, len(others)):
            backtrack(i+1, path + [others[i]])

    backtrack(0, [x])
    return result

def power_set(nums):
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result

if __name__ == "__main__":
    print(subsets_containing([2,3,4,5], 3))
    print(power_set([1,2,3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(power_set([0]))      # [[],[0]]
