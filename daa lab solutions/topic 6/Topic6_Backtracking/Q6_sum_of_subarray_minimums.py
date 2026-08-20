def sum_subarray_mins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    stack = []
    left = [0]*n   # distance to previous strictly smaller element
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    stack = []
    right = [0]*n  # distance to next smaller-or-equal element
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)
    total = 0
    for i in range(n):
        total += arr[i] * left[i] * right[i]
    return total % MOD

if __name__ == "__main__":
    print(sum_subarray_mins([3,1,2,4]))     # 17
    print(sum_subarray_mins([11,81,94,43,3]))  # 444
