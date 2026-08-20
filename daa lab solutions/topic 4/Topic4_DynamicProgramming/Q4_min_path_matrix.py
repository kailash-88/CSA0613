# "Minimum path distance" here is taken as the minimum-cost Hamiltonian
# cycle (Travelling Salesperson) over the given distance matrix, solved
# with the Held-Karp dynamic-programming algorithm (O(n^2 * 2^n)).
def tsp_dp(matrix):
    n = len(matrix)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = matrix[0][k]
    for subset_size in range(2, n):
        for subset in __import__('itertools').combinations(range(1, n), subset_size):
            bits = 0
            for b in subset:
                bits |= (1 << b)
            for k in subset:
                prev = bits & ~(1 << k)
                C[(bits, k)] = min(
                    C[(prev, m)] + matrix[m][k] for m in subset if m != k
                )
    bits = (1 << n) - 2
    return min(C[(bits, k)] + matrix[k][0] for k in range(1, n))

if __name__ == "__main__":
    m1 = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    print(tsp_dp(m1))  # 80
    m2 = [[0,10,10,10],[10,0,10,10],[10,10,0,10],[10,10,10,0]]
    print(tsp_dp(m2))  # 40
    m3 = [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
    print(tsp_dp(m3))  # 14 (the exercise sheet's expected 12 does not match any Hamiltonian cycle of this matrix)
