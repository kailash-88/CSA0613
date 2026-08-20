def find_paths(m, n, N, i, j):
    MOD = 10**9 + 7
    memo = {}
    def dp(steps, r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1
        if steps == 0:
            return 0
        if (steps, r, c) in memo:
            return memo[(steps, r, c)]
        total = 0
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            total = (total + dp(steps-1, r+dr, c+dc)) % MOD
        memo[(steps, r, c)] = total
        return total
    return dp(N, i, j)

if __name__ == "__main__":
    print(find_paths(2,2,2,0,0))  # 6
    print(find_paths(1,3,3,0,1))  # 12
