def find_target_sum_ways(nums, target):
    memo = {}
    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in memo:
            return memo[(i, total)]
        res = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        memo[(i, total)] = res
        return res
    return backtrack(0, 0)

if __name__ == "__main__":
    print(find_target_sum_ways([1,1,1,1,1], 3))  # 5
    print(find_target_sum_ways([1], 1))            # 1
