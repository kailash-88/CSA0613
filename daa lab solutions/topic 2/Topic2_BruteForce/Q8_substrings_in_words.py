def string_matching(words):
    result = []
    for i, w in enumerate(words):
        for j, other in enumerate(words):
            if i != j and w in other:
                result.append(w)
                break
    return result

if __name__ == "__main__":
    print(string_matching(["mass","as","hero","superhero"]))  # ['as','hero']
    print(string_matching(["leetcode","et","code"]))          # ['et','code']
    print(string_matching(["blue","green","bu"]))             # []
