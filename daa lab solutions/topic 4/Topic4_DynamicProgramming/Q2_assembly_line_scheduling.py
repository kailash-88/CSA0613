def assembly_line(a1, a2, t1, t2, e1, e2, x1, x2):
    n = len(a1)
    f1 = [0]*n
    f2 = [0]*n
    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]
    for i in range(1, n):
        f1[i] = min(f1[i-1] + a1[i], f2[i-1] + t2[i-1] + a1[i])
        f2[i] = min(f2[i-1] + a2[i], f1[i-1] + t1[i-1] + a2[i])
    return min(f1[n-1] + x1, f2[n-1] + x2)

if __name__ == "__main__":
    a1 = [4,5,3,2]
    a2 = [2,10,1,4]
    t1 = [3,1,3]
    t2 = [2,2,1]
    e1, e2 = 10, 12
    x1, x2 = 18, 7
    print("Minimum time:", assembly_line(a1, a2, t1, t2, e1, e2, x1, x2))
