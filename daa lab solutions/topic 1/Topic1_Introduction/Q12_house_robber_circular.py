def rob_line(nums):
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr

def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_line(nums[1:]), rob_line(nums[:-1]))

if __name__ == "__main__":
    print(rob_circular([2,3,2]))    # 3
    print(rob_circular([1,2,3,1]))  # 4
