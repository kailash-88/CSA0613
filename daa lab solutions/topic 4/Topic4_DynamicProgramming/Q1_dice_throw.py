def dice_throw_ways(num_sides, num_dice, target):
    dp = [[0]*(target+1) for _ in range(num_dice+1)]
    dp[0][0] = 1
    for dice in range(1, num_dice+1):
        for s in range(1, target+1):
            for face in range(1, num_sides+1):
                if s - face >= 0:
                    dp[dice][s] += dp[dice-1][s-face]
    return dp[num_dice][target]

if __name__ == "__main__":
    print("Number of ways to reach sum 7:", dice_throw_ways(6, 2, 7))    # 6
    print("Number of ways to reach sum 10:", dice_throw_ways(4, 3, 10))  # 27
