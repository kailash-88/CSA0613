from collections import defaultdict

def four_sum_count(A, B, C, D):
    sums_ab = defaultdict(int)
    for a in A:
        for b in B:
            sums_ab[a+b] += 1
    count = 0
    for c in C:
        for d in D:
            count += sums_ab.get(-(c+d), 0)
    return count

if __name__ == "__main__":
    print(four_sum_count([1,2],[-2,-1],[-1,2],[0,2]))  # 2
    print(four_sum_count([0],[0],[0],[0]))              # 1
