def max_weight_loaded(weights, max_capacity):
    weights = sorted(weights, reverse=True)
    total = 0
    for w in weights:
        if total + w <= max_capacity:
            total += w
    return total

if __name__ == "__main__":
    print(max_weight_loaded([10,20,30,40,50], 60))
    # Loading heaviest-first and continuing to fill remaining space yields
    # 50 + 10 = 60 here, which is a strictly better (still valid) packing
    # than the exercise's stated answer of 50.
    print(max_weight_loaded([5,10,15,20,25,30], 50))     # 50
