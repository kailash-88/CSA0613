def can_segment(s, word_dict):
    words = set(word_dict)
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]

if __name__ == "__main__":
    d = {"i","like","sam","sung","samsung","mobile","ice","cream","icecream","man","go","mango"}
    print("Yes" if can_segment("ilike", d) else "No")            # Yes
    print("Yes" if can_segment("ilikesamsung", d) else "No")     # Yes
