def word_break(s, word_dict):
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
    print(word_break("leetcode", ["leet","code"]))               # True
    print(word_break("applepenapple", ["apple","pen"]))           # True
    print(word_break("catsandog", ["cats","dog","sand","and","cat"]))  # False
