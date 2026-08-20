class WordFilter:
    def __init__(self, words):
        self.best = {}
        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n+1):
                prefix = word[:i]
                for j in range(n+1):
                    suffix = word[j:]
                    self.best[(prefix, suffix)] = idx  # later index overwrites -> largest index kept

    def f(self, pref, suff):
        return self.best.get((pref, suff), -1)

if __name__ == "__main__":
    wf = WordFilter(["apple"])
    print(wf.f("a", "e"))  # 0
