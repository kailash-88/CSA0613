def combination_sum(candidates, target):
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result

if __name__ == "__main__":
    print(combination_sum([2,3,6,7], 7))   # [[2,2,3],[7]]
    print(combination_sum([2,3,5], 8))     # [[2,2,2,2],[2,3,3],[3,5]]
