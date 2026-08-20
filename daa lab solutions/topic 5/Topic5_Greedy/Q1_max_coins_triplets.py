def max_coins(piles):
    piles.sort()
    n = len(piles) // 3
    total = 0
    # After sorting ascending: the smallest n piles always go to Bob.
    # Among the remaining 2n piles, Alice always takes the largest
    # remaining pile, so greedily taking every second-largest pile
    # (from the top, skipping one for Alice each time) maximizes yours.
    j = len(piles) - 2
    for _ in range(n):
        total += piles[j]
        j -= 2
    return total

if __name__ == "__main__":
    print(max_coins([2,4,1,2,7,8]))  # 9
    print(max_coins([2,4,5]))        # 4
