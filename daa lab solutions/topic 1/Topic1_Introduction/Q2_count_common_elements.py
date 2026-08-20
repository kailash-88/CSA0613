def count_common(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    answer1 = sum(1 for x in nums1 if x in set2)
    answer2 = sum(1 for x in nums2 if x in set1)
    return [answer1, answer2]

if __name__ == "__main__":
    print(count_common([2,3,2],[1,2]))              # [2,1]
    print(count_common([4,3,2,3,1],[2,2,5,2,3,6]))   # [3,4]
