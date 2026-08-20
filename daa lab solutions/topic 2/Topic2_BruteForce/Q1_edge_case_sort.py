def sort_list(lst):
    return sorted(lst)

if __name__ == "__main__":
    print(sort_list([]))                    # []
    print(sort_list([1]))                   # [1]
    print(sort_list([7,7,7,7]))              # [7,7,7,7]
    print(sort_list([-5,-1,-3,-2,-4]))       # [-5,-4,-3,-2,-1]
