def permute(nums):
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
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

if __name__ == "__main__":
    print(permute([1,2,3]))
    print(permute([0,1]))
    print(permute([1]))
