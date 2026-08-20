def unique_elements(nums):
    # Using a set gives O(n) time, O(n) space complexity
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
# Space complexity: O(n) - extra set + output list proportional to distinct elements

if __name__ == "__main__":
    print(unique_elements([3,7,3,5,2,5,9,2]))       # [3,7,5,2,9]
    print(unique_elements([-1,2,-1,3,2,-2]))         # [-1,2,3,-2]
    print(unique_elements([1000000,999999,1000000])) # [1000000,999999]
