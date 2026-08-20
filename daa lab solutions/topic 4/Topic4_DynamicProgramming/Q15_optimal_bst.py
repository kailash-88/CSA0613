def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            total = sum(freq[i:j+1])
            for r in range(i, j+1):
                left = cost[i][r-1] if r > i else 0
                right = cost[r+1][j] if r < j else 0
                c = left + right + total
                if c < cost[i][j]:
                    cost[i][j] = c
    return cost[0][n-1]

if __name__ == "__main__":
    keys = ['A','B','C','D']
    freq = [0.1, 0.2, 0.4, 0.3]
    print(round(optimal_bst(keys, freq), 2))  # 1.7

    print(optimal_bst([10,12], [34,50]))          # 118
    print(optimal_bst([10,12,20], [34,8,50]))     # 142
