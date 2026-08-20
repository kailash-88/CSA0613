def combination_sum2(candidates, target):
    candidates.sort()
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i+1, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result

if __name__ == "__main__":
    print(combination_sum2([10,1,2,7,6,1,5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(combination_sum2([2,5,2,1,2], 5))         # [[1,2,2],[5]]
