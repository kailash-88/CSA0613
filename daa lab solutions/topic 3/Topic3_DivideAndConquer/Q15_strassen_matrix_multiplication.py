def strassen_2x2(A, B):
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    e, f = B[0][0], B[0][1]
    g, h = B[1][0], B[1][1]

    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    return [[c11, c12], [c21, c22]]

if __name__ == "__main__":
    A = [[1,7],[3,5]]
    B = [[1,3],[7,5]]
    print(strassen_2x2(A, B))  # [[50,38],[38,34]]

    A2 = [[1,7],[3,5]]
    B2 = [[6,8],[4,2]]
    print(strassen_2x2(A2, B2))  # [[34,22],[38,34]] -- verify below
