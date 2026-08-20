def str_str(haystack, needle):
    return haystack.find(needle)

if __name__ == "__main__":
    print(str_str("sadbutsad", "sad"))   # 0
    print(str_str("leetcode", "leeto"))  # -1
