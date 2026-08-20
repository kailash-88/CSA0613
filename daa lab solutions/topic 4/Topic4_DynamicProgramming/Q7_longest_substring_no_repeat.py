def length_of_longest_substring(s):
    last_seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))      # 1
    print(length_of_longest_substring("pwwkew"))     # 3
