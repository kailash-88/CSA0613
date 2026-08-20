def min_add_to_make_all_obtainable(coins, target):
    coins = sorted(coins)
    miss = 0
    reach = 0  # can make every integer in [1, reach] using current coins
    i = 0
    n = len(coins)
    while reach < target:
        if i < n and coins[i] <= reach + 1:
            reach += coins[i]
            i += 1
        else:
            reach += reach + 1  # add coin of value reach+1
            miss += 1
    return miss

if __name__ == "__main__":
    print(min_add_to_make_all_obtainable([1,4,10], 19))              # 2
    print(min_add_to_make_all_obtainable([1,4,10,5,7,19], 19))       # 1
