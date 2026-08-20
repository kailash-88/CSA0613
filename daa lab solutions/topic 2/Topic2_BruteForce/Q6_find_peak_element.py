def find_peak_element(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid+1]:
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    print(find_peak_element([1,2,3,1]))          # 2
    print(find_peak_element([1,2,1,3,5,6,4]))    # 1 or 5
