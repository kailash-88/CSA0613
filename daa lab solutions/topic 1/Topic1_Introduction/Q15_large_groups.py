def large_groups(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i >= 3:
            result.append([i, j-1])
        i = j
    return result

if __name__ == "__main__":
    print(large_groups("abbxxxxzzy"))  # [[3,6]]
    print(large_groups("abc"))         # []
