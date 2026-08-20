def permute_unique(nums):
    nums.sort()
    result = []
    path = []
    used = [False]*len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

if __name__ == "__main__":
    print(permute_unique([1,1,2]))    # [[1,1,2],[1,2,1],[2,1,1]]
    print(permute_unique([1,2,3]))
