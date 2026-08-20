from collections import Counter

def word_subsets(words1, words2):
    max_req = Counter()
    for w in words2:
        c = Counter(w)
        for ch, cnt in c.items():
            max_req[ch] = max(max_req[ch], cnt)

    result = []
    for w in words1:
        c = Counter(w)
        if all(c[ch] >= cnt for ch, cnt in max_req.items()):
            result.append(w)
    return result

if __name__ == "__main__":
    print(word_subsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
    print(word_subsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
