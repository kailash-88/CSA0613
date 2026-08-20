def sort_then_max(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)  # efficient sort O(n log n)
    return sorted_lst[-1]

if __name__ == "__main__":
    print(sort_then_max([]))            # None
    print(sort_then_max([5]))           # 5
    print(sort_then_max([3,3,3,3,3]))   # 3
