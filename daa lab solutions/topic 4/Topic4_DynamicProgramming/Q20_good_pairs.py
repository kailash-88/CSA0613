def num_good_pairs(nums):
    from collections import Counter
    c = Counter(nums)
    return sum(v*(v-1)//2 for v in c.values())

if __name__ == "__main__":
    print(num_good_pairs([1,2,3,1,1,3]))  # 4
    print(num_good_pairs([1,1,1,1]))      # 6
